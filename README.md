# 📄 PDF Viewer

> **Preview PDF files directly inside Discord using Discord's native image gallery.**

PDF Viewer lets you read PDF documents without downloading them. Simply upload a PDF, run the `/preview` command, and browse pages in Discord's fullscreen image viewer using your keyboard's arrow keys.

<p align="center">
  <img src="https://raw.githubusercontent.com/Dipson-bot/discord-pdf-viewer-bot/main/pdf-viewer-demo.gif" width="900" alt="PDF Viewer Demo">
</p>

<p align="center">
  <strong>Made by Dipson</strong>
</p>

---

## ✨ Features

- 📄 Preview PDF files directly inside Discord
- 🔍 Search uploaded PDFs by filename
- 🖼️ Uses Discord's native fullscreen image gallery
- ⌨️ Navigate pages using the **←** and **→** arrow keys
- ⚡ Fast multi-threaded PDF rendering
- 🔒 Ephemeral previews (only visible to the user)
- 🌍 Supports multiple Discord servers
- 🚀 Optional automatic startup with Windows
- 💻 One-click Windows startup installer included
- 📚 No need to download PDFs before reading

---

## 📋 Requirements

- Python 3.10 or newer
- Windows 10/11 (tested)
- A Discord Bot Token
- Internet connection

---

# 🚀 Quick Start

If you're already familiar with Discord bots:

```bash
git clone https://github.com/Dipson-bot/discord-pdf-viewer-bot.git

cd discord-pdf-viewer-bot

pip install -r requirements.txt

python bot.py
```

If you're new to Discord bot development, continue with the detailed installation guide below.

---

# 📦 Installation Guide

## 1. Install Python

Download Python from:

https://www.python.org/downloads/

During installation, make sure to enable:

✅ **Add Python to PATH**

---

## 2. Download the Project

Clone the repository:

```bash
git clone https://github.com/Dipson-bot/discord-pdf-viewer-bot.git
```

or click the green **Code** button on GitHub and download the ZIP.

---

## 3. Install Required Packages

Open a terminal inside the project folder.

Run:

```bash
pip install -r requirements.txt
```

---

# 🤖 Create a Discord Bot

1. Visit:

https://discord.com/developers/applications

2. Click **New Application**

3. Enter any name you like.

4. Open the **Bot** tab.

5. Click **Add Bot**.

6. Click **Reset Token** (or **Copy Token** if it's a brand new bot).

⚠️ **Never share your bot token with anyone.**

---

# 🔑 Configure the Bot Token

The repository includes:

```
.env.example
```

Copy this file.

Rename the copy to:

```
.env
```

Open `.env`.

Replace:

```text
DISCORD_TOKEN=YOUR_DISCORD_BOT_TOKEN_HERE
```

with your own bot token.

Example:

```text
DISCORD_TOKEN=MTExXXXXXXXXXXXXXXXXXXXXXXXXXXXX
```

---

# ⚙️ Enable Required Bot Settings

Inside the Discord Developer Portal:

Open your application.

Go to:

**Bot**

Enable:

- ✅ Message Content Intent

Save the changes.

---

# 📨 Invite the Bot

Go to:

**OAuth2 → Installation**

Choose:

**Guild Install**

For permissions, **Administrator** is recommended while testing.

Copy the generated invite link.

Open it in your browser.

Choose your Discord server.

Click **Authorize**.

---

# ▶️ Start the Bot

Run:

```bash
python bot.py
```

If everything is working correctly you should see something similar to:

```text
Synced 1 global command(s)
PDF Viewer Bot online
```

---

# 🚀 Start Automatically with Windows (Optional)

The easiest way to keep the bot running automatically after every Windows login is to use the included installer.

Simply double-click:

```
install_startup.bat
```

The installer will automatically create a Windows Scheduled Task that:

- ✅ Starts the bot whenever you log into Windows
- ✅ Runs the bot in the background (no Command Prompt window)
- ✅ Waits for an internet connection before launching
- ✅ Uses the correct project folder automatically

> **No manual Task Scheduler configuration is required.**

If you ever want to disable automatic startup, simply run:

```
uninstall_startup.bat
```

> **Note:** The Discord desktop application does **not** need to be running. The bot connects directly to Discord using your bot token.

> **Note:** You can keep the bot folder anywhere on your computer (Desktop, Documents, Downloads, another drive, etc.). The installer automatically detects its location.
>
> If you move the bot folder after running `install_startup.bat`, simply run:
>
> ```
> uninstall_startup.bat
> install_startup.bat
> ```
>
> again to update the startup task to the new location.

# 📖 Using the Bot

1. Upload a PDF to a Discord channel.

2. Type:

```
/preview
```

3. Select the PDF.

4. Wait while the bot renders the pages.

5. Click any page.

6. Open Discord's fullscreen viewer.

7. Use the **←** and **→** arrow keys to navigate between pages.

---

# ⚙️ Configuration

You can customize the bot by editing `config.py`.

| Setting | Description |
|---------|-------------|
| DPI | PDF rendering quality |
| MAX_FILE_MB | Maximum allowed PDF size |
| ALLOWED_CHANNELS | Restrict the bot to specific channel IDs |

---

# ❓ Frequently Asked Questions

### `/preview` doesn't appear.

Global slash commands may take several minutes (sometimes up to one hour) to appear.

Restart the bot if necessary.

---

### "DISCORD_TOKEN environment variable is not set."

Make sure you created:

```
.env
```

and that it contains:

```text
DISCORD_TOKEN=YOUR_BOT_TOKEN
```

---

### The bot can't find my PDF.

The bot only searches PDF files uploaded in the current Discord channel.

---

### The PDF is too large.

Increase:

```
MAX_FILE_MB
```

inside `config.py`.

---

### Do I need to keep Discord open?

**No.**

The bot connects directly to Discord using your bot token.

As long as your computer is running, connected to the internet, and `python bot.py` is running, the bot will stay online.

---

# ⚠️ Known Limitations

The bot is designed to be lightweight and easy to use. A few limitations currently exist:

- 📂 The bot only searches for PDF files uploaded in the **current Discord channel**.
- ⏳ Global slash commands may take several minutes (sometimes up to **one hour**) to appear after inviting the bot to a server.
- 📄 Large PDFs may take longer to render depending on the number of pages, rendering DPI, and your computer's performance.
- 📦 The maximum PDF size is controlled by `MAX_FILE_MB` in `config.py` (default: **50 MB**).
- 🖼️ Discord only allows **10 attachments per message**, so PDFs with more than 10 pages are automatically split into multiple ephemeral messages.
- 🪟 Automatic startup on Windows is supported using `run_bot.bat`, but **you must place a shortcut to the batch file in the Startup folder, not a copy of the file itself.**
- 🌐 The bot must be running on a computer with an active internet connection. Closing the Python process or shutting down the computer will take the bot offline.
- 🔒 Only users with permission to use slash commands in a server can access the bot's commands.

---

# 🛣️ Roadmap

- [ ] Jump directly to a page
- [ ] Zoom controls
- [ ] Docker support
- [ ] Password-protected PDFs
- [ ] Public hosted version
- [ ] Multiple rendering presets

---

# 🤝 Contributing

Contributions, bug reports, and feature requests are always welcome.

Feel free to open an Issue or submit a Pull Request.

---

# 📜 License

This project is licensed under the MIT License.

---

<p align="center">

⭐ **If this project helped you, consider giving it a star!**

Made by **Dipson**

</p>