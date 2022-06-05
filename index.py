from telethon import TelegramClient, events, sync

# Remember to use your own values from my.telegram.org!
api_id = '1234567'
api_hash = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
client = TelegramClient('anon', api_id, api_hash)

print("Running....")


@client.on(events.NewMessage(chats='Group Name'))
async def my_event_handler(event):
    customtxt = event.raw_text
    customtxt = customtxt.lower()
    if "go" in customtxt:
        print(customtxt, "FOUND")
        await client.send_message('Username', 'VISA Available')
    else:
        abcd = 1
        

client.start()
client.run_until_disconnected()

#+9779818285223
