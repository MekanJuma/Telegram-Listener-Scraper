# Telegram Scraper and Listener

This project consists of two Python scripts that interact with Telegram using the Telethon library. One script extracts historical messages from specified Telegram groups, and the other listens for new messages in specific groups and forwards them to a Discord channel via a webhook.

# Features
- Extract historical messages from Telegram groups.
- Listen to specific (or all) Telegram groups and forward new messages to a Discord channel.
- Handle message attachments and formatting.

## Prerequisites
- Python 3.6 or above
- [Telethon](https://docs.telethon.dev/en/latest/)
- [discord](https://discordpy.readthedocs.io/en/stable/)

Install the required libraries using pip:
```
pip install telethon discord
```

# Scripts
**1. scraper.py**
This script extracts historical messages from specified Telegram groups.
```
python scraper.py
```
When you run the script, follow the prompts to input the necessary information such as the Telegram group URL.

**2. listener.py**
This script listens to specified Telegram groups for new incoming messages and sends them to a Discord channel via a webhook.
```
python listener.py
```

# Configurations
Both scripts require a **config.ini** file with the necessary Telegram credentials and other configurations. Here’s a sample structure for your config.ini file:
```
[TelegramCredentials]
api_id = YOUR_API_ID
api_hash = YOUR_API_HASH
phone = YOUR_PHONE_NUMBER
username = YOUR_USERNAME
```
Make sure to replace the placeholders with your actual Telegram API credentials.

# Follow me on these channels
- [My Telegram Group](https://t.me/pythonowreneli)
- [My Youtube Channel](https://www.youtube.com/@MekanJuma/videos)
- [My Instagram](https://www.instagram.com/jumaevmekan/)
- [LinkIn](https://www.linkedin.com/in/mekan-jumayev/)
