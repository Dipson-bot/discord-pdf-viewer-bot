from dotenv import load_dotenv
import os

load_dotenv()

# Your Discord bot token
#TOKEN = os.getenv("DISCORD_TOKEN", "YOUR BOT TOKEN HERE")
TOKEN = os.getenv("DISCORD_TOKEN")
if TOKEN is None:
    raise RuntimeError("DISCORD_TOKEN environment variable is not set.")
# Your Discord Server ID
# GUILD_ID = 1272024414124380190
# Render quality for Discord preview: 200=sharp, 150=balanced
DPI = 200

# Max PDF file size in MB
MAX_FILE_MB = 50

# Local port for the browser viewer web server
WEB_PORT = 8765

# Restrict to specific channel IDs (empty = all channels)
ALLOWED_CHANNELS = []
