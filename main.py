#    https://github.com/yltcode/telegram-auto-comment
#    Copyright (C) 2022-present  dently

#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.

#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.

#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <https://www.gnu.org/licenses/>.

import os
import yaml
import random

from pyrogram import Client, filters
from pyrogram.types import Message
from pyrogram.errors import MsgIdInvalid

import logging

logging.basicConfig(level=logging.INFO)

if os.path.exists("session.session-journal"):
    os.remove("session.session-journal")

with open("config.yaml", "r", encoding="utf-8") as file:
    config = yaml.safe_load(file)

api_id = config["api_id"]
api_hash = config["api_hash"]
messages = config["messages"]

app = Client(
    "session",
    api_id,
    api_hash
)

with app:
    me = app.get_me()
    logging.info("Started for {name}", name=me.first_name)


@app.on_message(filters.channel & ~filters.me)
async def handler(app: Client, message: Message):
    try:
        text = random.choice(messages)
        msg = await app.get_discussion_message(
            message.chat.id, message.id
        )
        await msg.reply(text)
    except MsgIdInvalid:
        ...


if __name__ == "__main__":
    app.run()
