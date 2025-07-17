import os
import json
import logging
from datetime import datetime
from pathlib import Path
from dotenv import load_dotenv
from telethon import TelegramClient
from telethon.errors import SessionPasswordNeededError
from telethon.tl.types import MessageMediaPhoto

# Load environment variables
load_dotenv()
API_ID = os.getenv('TELEGRAM_API_ID')
API_HASH = os.getenv('TELEGRAM_API_HASH')
BOT_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')

# Configure logging
LOG_DIR = Path('logs')
LOG_DIR.mkdir(exist_ok=True)
logging.basicConfig(
    filename=LOG_DIR / 'scrape_telegram.log',
    level=logging.INFO,
    format='%(asctime)s %(levelname)s %(message)s'
)

# Channels to scrape
CHANNELS = [
    'https://t.me/lobelia4cosmetics',
    'https://t.me/tikvahpharma',
    # Add more channels as needed
]

RAW_DATA_DIR = Path('data/raw/telegram_messages')
IMAGES_DIR = Path('data/raw/telegram_images')

async def scrape_channel(client, channel_url):
    today = datetime.now().strftime('%Y-%m-%d')
    channel_name = channel_url.split('/')[-1]
    out_dir = RAW_DATA_DIR / today
    out_dir.mkdir(parents=True, exist_ok=True)
    images_out_dir = IMAGES_DIR / today / channel_name
    images_out_dir.mkdir(parents=True, exist_ok=True)
    messages = []
    try:
        async for message in client.iter_messages(channel_url, limit=1000):
            msg_dict = message.to_dict()
            # Download images if present
            if message.media and isinstance(message.media, MessageMediaPhoto):
                image_path = images_out_dir / f"{message.id}.jpg"
                await client.download_media(message, file=image_path)
                msg_dict['downloaded_image_path'] = str(image_path)
            messages.append(msg_dict)
        # Save messages as JSON
        with open(out_dir / f"{channel_name}.json", 'w', encoding='utf-8') as f:
            json.dump(messages, f, ensure_ascii=False, indent=2)
        logging.info(f"Scraped {len(messages)} messages from {channel_name}")
    except Exception as e:
        logging.error(f"Error scraping {channel_name}: {e}")

async def main():
    client = TelegramClient('anon', API_ID, API_HASH)
    await client.start(bot_token=BOT_TOKEN)
    for channel in CHANNELS:
        await scrape_channel(client, channel)
    await client.disconnect()

if __name__ == '__main__':
    import asyncio
    asyncio.run(main()) 