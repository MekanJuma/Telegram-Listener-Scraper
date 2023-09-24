from telethon import TelegramClient, errors
from telethon.tl.functions.messages import GetHistoryRequest
from telethon.tl.types import PeerChannel


import configparser
import json
from datetime import datetime


class DateTimeEncoder(json.JSONEncoder):
    """Custom JSON Encoder to handle datetime objects and bytes."""
    
    def default(self, o):
        if isinstance(o, datetime):
            return o.isoformat()
        if isinstance(o, bytes):
            return list(o)
        return super().default(o)


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

async def sign_in(client, phone):
    """Handle user sign-in to Telegram."""
    if not await client.is_user_authorized():
        await client.send_code_request(phone)
        try:
            await client.sign_in(phone, input('Enter the code: '))
        except errors.SessionPasswordNeededError:
            await client.sign_in(password=input('Password: '))

async def fetch_all_messages(client, entity):
    """Fetch all messages from a given entity."""
    offset_id = 0
    limit = 100
    all_messages = []

    while True:
        history = await client(GetHistoryRequest(            
            peer=entity,
            offset_id=offset_id,
            offset_date=None,
            add_offset=0,
            limit=limit,
            max_id=0,
            min_id=0,
            hash=0
        ))
        if not history.messages:
            break

        all_messages.extend(history.messages)
        offset_id = history.messages[-1].id

    return [message.to_dict() for message in all_messages]

async def main(client):
    """Main asynchronous function."""
    configs = read_configs()

    await client.start()
    await sign_in(client, configs['phone'])

    channel_url = 'https://t.me/pythonowreneli'
    entity = PeerChannel(int(channel_url)) if channel_url.isdigit() else channel_url
    messages = await fetch_all_messages(client, await client.get_entity(entity))

    with open('channel_messages.json', 'w') as outfile:
        json.dump(messages, outfile, cls=DateTimeEncoder)
    
    await client.disconnect()
    
    
if __name__ == '__main__':
    configs = read_configs()
    with TelegramClient(configs['username'], configs['api_id'], configs['api_hash']) as client:
        client.loop.run_until_complete(main(client))