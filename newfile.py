from telethon import TelegramClient, events
from handlers import text_handler
# Replace these values with your own API ID, API hash, and phone number
api_id = 1150846
api_hash = "d50ee5d1e6ba3b7950f3c38f08935f6f"

client = TelegramClient('session_name', api_id, api_hash)

async def forward_messages(event):
        destination = 541004638
        await client.edit_message(destination, event.message, "Hello there" )

client.start()
client.run_until_disconnected()

