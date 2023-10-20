from telethon import TelegramClient, events

# Replace these values with your own API ID, API hash, and phone number
api_id = 1150846
api_hash = "d50ee5d1e6ba3b7950f3c38f08935f6f"

client = TelegramClient('session_name', api_id, api_hash)

@client.on(events.NewMessage(outgoing=True, pattern=".hi"))
async def assalomu_alaykum(event):
        await client.edit_message(event.message, "Assalomu alaykum" )

client.start()
client.run_until_disconnected()

