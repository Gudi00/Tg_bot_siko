#
# from pyrogram import Client, filters
#
# API_ID = '26118223'
# API_HASH = '8423f1b169ea4515e0b2b5127fc92da0'
# PHONE_NUMBER = '+375257661287'
#
# app = Client("my_account", api_id=API_ID, api_hash=API_HASH, phone_number=PHONE_NUMBER)
#
# @app.on_message(filters.text & filters.group)
# async def reply_to_hello(client, message):
#     if 'привет' in message.text.lower():
#         await message.reply("привет")
#
# app.run()

import asyncio
import uvloop
from pyrogram import Client

from pyrogram import Client


async def main():
    app = Client("my_account")

    async with app:
        print(await app.get_me())


uvloop.install()
asyncio.run(main())



uvloop.install()

app = Client("my_account")


@app.on_message()
async def hello(client, message):
    print(await client.get_me())


app.run()