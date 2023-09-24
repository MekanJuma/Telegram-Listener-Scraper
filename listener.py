from telethon import TelegramClient, events
from discord import SyncWebhook, File
from datetime import datetime

import re, configparser

webhook_url = 'YOUR_WEBHOOK_URL'

def read_configs():
    """Read configurations from 'config.ini' file."""
    config = configparser.ConfigParser()
    config.read("config.ini")

    return {
        'api_id': config.get('TelegramCredentials', 'api_id'),
        'api_hash': config.get('TelegramCredentials', 'api_hash'),
        'phone': config.get('TelegramCredentials', 'phone'),
        'username': config.get('TelegramCredentials', 'username'),
    }

def send_msg_discord(msg, attachment=False):
    """ You can refactor this function better and dynamic"""
    webhook = SyncWebhook.from_url(webhook_url)
    if attachment:
        with open('img.png', 'rb') as file:
            webhook.send(msg, file=File(file, filename="display_file_name.png"))
    else:
        webhook.send(msg)

configs = read_configs()
client = TelegramClient(configs['username'], configs['api_id'], configs['api_hash'])

def extract_numbers_from_string(s):
    """Extract numbers from a string and return them as a list."""
    return re.findall(r'\d+', s)

@client.on(events.NewMessage(chats='groupname or id'))
# @client.on(events.NewMessage(pattern='(.*?)'))
async def my_event_handler(event):
    sender = await event.get_sender()

    data = {
        "Chat ID": event.chat_id,
        "Message": event.message.message,
        "Message ID": event.message.id,
        "Username": sender.username,
        "Peer ID": extract_numbers_from_string(str(event.message.peer_id)),
        "From ID": extract_numbers_from_string(str(event.message.from_id)),
        "Datetime": str(datetime.now())
    }
    send_msg_discord(data.get('Message', 'No message'))
    
    
if __name__ == "__main__":
    client.start()
    client.run_until_disconnected()