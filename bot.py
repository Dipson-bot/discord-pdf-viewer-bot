"""
Discord PDF Viewer Bot v9
- Uses Discord's native image gallery for fullscreen + arrow key navigation
- Renders pages and sends them as images in one message (up to 10 per message)
- All ephemeral - only visible to the user
- Fast rendering with parallel page processing
"""

import discord
from discord import app_commands
import fitz
import io
import asyncio
from concurrent.futures import ThreadPoolExecutor
from PIL import Image, ImageDraw
#from config import TOKEN, DPI, MAX_FILE_MB, GUILD_ID
from config import TOKEN, DPI, MAX_FILE_MB
import httpx

intents = discord.Intents.default()
intents.message_content = True
#MY_GUILD = discord.Object(id=GUILD_ID)

executor = ThreadPoolExecutor(max_workers=4)


class PDFBot(discord.Client):
    def __init__(self):
        super().__init__(intents=intents)
        self.tree = app_commands.CommandTree(self)

    #async def setup_hook(self):
       # self.tree.copy_global_to(guild=MY_GUILD)
        #synced = await self.tree.sync(guild=MY_GUILD)
       # print(f"   Synced {len(synced)} command(s) ✅")

    async def setup_hook(self):
        synced = await self.tree.sync()
        print(f"Synced {len(synced)} global command(s)")

client = PDFBot()


# ── Rendering ─────────────────────────────────────────────────────────────────

def render_page_bytes(args) -> bytes:
    """Render a single page to JPEG bytes. Runs in thread pool."""
    pdf_bytes, page_num, total, dpi = args
    doc = fitz.open(stream=pdf_bytes, filetype="pdf")
    page = doc[page_num]
    pix = page.get_pixmap(matrix=fitz.Matrix(dpi/72, dpi/72), alpha=False)
    img = Image.frombytes("RGB", (pix.width, pix.height), pix.samples)
    doc.close()

    # Add subtle page label at bottom
    bar_h = 32
    out = Image.new("RGB", (img.width, img.height + bar_h), (30, 31, 34))
    out.paste(img, (0, 0))
    draw = ImageDraw.Draw(out)
    draw.text(
        (img.width // 2, img.height + 8),
        f"Page {page_num + 1} / {total}",
        fill=(170, 170, 170), anchor="mt"
    )
    buf = io.BytesIO()
    out.save(buf, format="JPEG", quality=88, optimize=True)
    return buf.getvalue()


async def render_all_pages(pdf_bytes: bytes, total: int, dpi: int) -> list[bytes]:
    """Render all pages in parallel using thread pool."""
    loop = asyncio.get_event_loop()
    args = [(pdf_bytes, i, total, dpi) for i in range(total)]
    tasks = [loop.run_in_executor(executor, render_page_bytes, a) for a in args]
    return await asyncio.gather(*tasks)


# ── Helpers ───────────────────────────────────────────────────────────────────

async def fetch_pdfs_in_channel(channel, limit=500):
    found, seen = [], set()
    async for msg in channel.history(limit=limit):
        for att in msg.attachments:
            if att.filename.lower().endswith(".pdf") and att.filename not in seen:
                found.append(att)
                seen.add(att.filename)
    return found


def pages_to_files(page_bytes_list: list[bytes], start: int) -> list[discord.File]:
    """Convert rendered page bytes to discord.File objects."""
    files = []
    for i, b in enumerate(page_bytes_list):
        page_num = start + i + 1
        files.append(discord.File(
            io.BytesIO(b),
            filename=f"page_{page_num:04d}.jpg",  # zero-padded for correct ordering
            description=f"Page {page_num}"
        ))
    return files


# ── /preview command ──────────────────────────────────────────────────────────

@client.tree.command(name="preview", description="Preview a PDF from this channel")
@app_commands.describe(filename="Start typing to search PDFs in this channel")
async def preview_cmd(interaction: discord.Interaction, filename: str):
    await interaction.response.defer(ephemeral=True)

    pdfs = await fetch_pdfs_in_channel(interaction.channel)
    match = next((p for p in pdfs if p.filename == filename), None)
    if not match:
        match = next((p for p in pdfs if filename.lower() in p.filename.lower()), None)
    if not match:
        await interaction.followup.send(
            f"❌ No PDF matching **'{filename}'** found.", ephemeral=True)
        return

    size_mb = match.size / (1024 * 1024)
    if size_mb > MAX_FILE_MB:
        await interaction.followup.send(
            f"⚠️ File is {size_mb:.1f} MB — limit is {MAX_FILE_MB} MB.", ephemeral=True)
        return

    await interaction.followup.send(
        f"⏳ Rendering **{match.filename}**...", ephemeral=True)

    try:
        # Download PDF
        async with httpx.AsyncClient(follow_redirects=True, timeout=120) as http:
            resp = await http.get(match.url)
            pdf_bytes = resp.content

        doc = fitz.open(stream=pdf_bytes, filetype="pdf")
        total = doc.page_count
        doc.close()

        await interaction.edit_original_response(
            content=f"⏳ Rendering {total} pages of **{match.filename}**..."
        )

        # Render all pages in parallel
        all_page_bytes = await render_all_pages(pdf_bytes, total, DPI)

        # Send in batches of 10 (Discord's max files per message)
        BATCH = 10
        num_batches = (total + BATCH - 1) // BATCH

        for batch_idx in range(num_batches):
            start = batch_idx * BATCH
            end = min(start + BATCH, total)
            batch = all_page_bytes[start:end]
            files = pages_to_files(batch, start)

            if batch_idx == 0:
                # First batch — edit the original ephemeral message
                label = (f"📄 **{match.filename}** — {total} pages\n"
                         f"{'Pages 1–' + str(end) if num_batches > 1 else 'All pages'} below ↓\n"
                         f"*Click any page → fullscreen → use ← → arrow keys to flip pages!*")
                await interaction.edit_original_response(
                    content=label,
                    attachments=files
                )
            else:
                # Subsequent batches — send as follow-up (also ephemeral)
                label = f"📄 **{match.filename}** — Pages {start+1}–{end}"
                await interaction.followup.send(
                    content=label,
                    files=files,
                    ephemeral=True
                )
            # Small delay between batches
            if batch_idx < num_batches - 1:
                await asyncio.sleep(1)

    except Exception as e:
        await interaction.edit_original_response(content=f"❌ Error: `{e}`")
        raise


@preview_cmd.autocomplete("filename")
async def preview_autocomplete(interaction: discord.Interaction, current: str):
    pdfs = await fetch_pdfs_in_channel(interaction.channel, limit=300)
    return [
        app_commands.Choice(name=p.filename[:100], value=p.filename)
        for p in pdfs if current.lower() in p.filename.lower()
    ][:25]


@client.event
async def on_ready():
    print(f"✅ PDF Viewer Bot online as {client.user}")
    print(f"   DPI: {DPI} | Using Discord native gallery")
    print(f"   Tip: Click any page → fullscreen → use ← → to navigate!")


def main():
    if not TOKEN or TOKEN == "YOUR_BOT_TOKEN_HERE":
        print("❌ Set token in config.py"); return
    client.run(TOKEN)

if __name__ == "__main__":
    main()
