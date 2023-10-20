from telethon import TelegramClient, event
client = client.client

@client.on(events.NewMessage(chats=541004638, outgoing=True))
async def textreturn(event):
	return event.message