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
import utils
import yaml
import random

from pyrogram import Client, filters
from pyrogram.types import Message
from pyrogram.errors import ChannelPrivate, MsgIdInvalid

import logging

logging.basicConfig(level=logging.ERROR)

path = os.path.realpath(__file__)
directory = os.path.dirname(path)

if directory != os.getcwd():
    os.chdir(directory)

with open("config.yml", "r", encoding="utf-8") as file:
    config = yaml.safe_load(file)

api_id = config["api_id"]
api_hash = config["api_hash"]
messages = config["messages"]

app = Client(
    "session",
    api_id,
    api_hash,
    app_version="3.7 x64",
    device_model="PC 64bit",
    system_version="Windows 10"
)

with app:
    me = app.get_me()
    print("Started for", me.first_name)


@app.on_message(filters.channel & ~filters.me)
async def handler(_, message: Message):
    try:
        post = await app.get_discussion_message(
            message.chat.id, message.id
        )

        if isinstance(messages, str):
            text = messages
        elif len(messages) == 1:
            [text] = messages
        else:
            text = random.choice(messages)

        chars_with_font = utils.make_text_with_font(text)
        text_with_font = "".join(chars_with_font)

        await post.reply(text_with_font)
    except (ChannelPrivate, MsgIdInvalid):
        ...


if __name__ == "__main__":
    app.run()
