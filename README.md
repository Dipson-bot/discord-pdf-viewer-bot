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

* 📄 Preview PDF files directly inside Discord
* 🔍 Search uploaded PDFs by filename
* 🖼️ Native Discord fullscreen image gallery
* ⌨️ Navigate pages using the **←** and **→** arrow keys
* ⚡ Fast multi-threaded rendering
* 🔒 Ephemeral previews (only visible to the user)
* 🌍 Supports multiple Discord servers
* 📚 No need to download the PDF before reading

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

Download and install Python from:

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

⚠️ Never share your bot token.

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

* ✅ Message Content Intent

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

# ▶ Start the Bot

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

# 📖 Using the Bot

1. Upload a PDF into a Discord channel.

2. Type:

```
/preview
```

3. Select the PDF.

4. Wait while the bot renders the pages.

5. Click any page.

6. Use Discord's fullscreen viewer.

7. Press **←** or **→** to move between pages.

---

# ⚙️ Configuration

You can edit these values inside `config.py`.

| Setting          | Description                           |
| ---------------- | ------------------------------------- |
| DPI              | Rendering quality                     |
| MAX_FILE_MB      | Maximum PDF size                      |
| ALLOWED_CHANNELS | Restrict the bot to specific channels |

---

# ❓ Frequently Asked Questions

### The `/preview` command doesn't appear.

Global slash commands may take several minutes (sometimes up to one hour) to appear.

Restart the bot if necessary.

---

### The bot says "DISCORD_TOKEN environment variable is not set."

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

# 🛣️ Roadmap

* [ ] Jump directly to a page
* [ ] Zoom controls
* [ ] Docker support
* [ ] Password-protected PDFs
* [ ] Public hosted version
* [ ] Multiple rendering presets

---

# 🤝 Contributing

Contributions are welcome.

Feel free to open an issue, suggest new features, or submit a pull request.

---

# 📜 License

This project is licensed under the MIT License.

---

<p align="center">

⭐ If this project helped you, consider giving it a star!

Made with ❤️ by **Dipson**

</p>
