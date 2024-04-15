from telethon import TelegramClient

api_id = "api_id" #or as a int
api_hash = "api hash"
client = TelegramClient('anon', api_id, api_hash)

async def main():
   users = await client.get_participants(group_ID)
   print(users[0].id)


with client:
   client.loop.run_until_complete(main())
