

import asyncio
import random

from pyrogram import filters
from pyrogram.enums import ChatType
from pyrogram.types import InlineKeyboardMarkup, Message


from nexichat import nexichat
from nexichat.database.chats import add_served_chat
from nexichat.database.users import add_served_user
from nexichat.modules.helpers import (
    CLOSE_BTN,
    DEV_OP,
    HELP_BTN,
    HELP_BUTN,
    HELP_READ,
    HELP_START,
    SOURCE_READ,
    START,
)


#----------------IMG-------------#



# Random Start Images
IMG = [
    "https://telegra.ph/file/d508f82183be944149e4f.jpg",
    "https://telegra.ph/file/8c276526481ae68a9250a.jpg",
    "https://telegra.ph/file/b1a60eb37babad1695caf.jpg",
    "https://telegra.ph/file/b1a60eb37babad1695caf.jpg",
    "https://telegra.ph/file/229174c9e856532bd39b6.jpg",
    "https://telegra.ph/file/c2cefef04a79b4ce65dfe.jpg",
    "https://telegra.ph/file/c615b8d5aa215d9e1fde0.jpg",
    "https://telegra.ph/file/c615b8d5aa215d9e1fde0.jpg",
    "https://telegra.ph/file/c2cefef04a79b4ce65dfe.jpg",
    "https://telegra.ph/file/c615b8d5aa215d9e1fde0.jpg",
    "https://telegra.ph/file/c615b8d5aa215d9e1fde0.jpg",
    "https://telegra.ph/file/229174c9e856532bd39b6.jpg",
    "https://telegra.ph/file/8c276526481ae68a9250a.jpg",
    "https://telegra.ph/file/d508f82183be944149e4f.jpg",
]


#----------------IMG-------------#


#---------------STICKERS---------------#

# Random Stickers
STICKER = [
    " CAACAgUAAx0CeFQzogACIUplxOnOXxb6KtZfSm4CJBOQJqqPjQACzwQAAtlm0VUo31i38D0Y0h4E",
    "CAACAgUAAx0CeFQzogACIUplxOnOXxb6KtZfSm4CJBOQJqqPjQACzwQAAtlm0VUo31i38D0Y0h4E",
    "CAACAgUAAx0CeFQzogACIUplxOnOXxb6KtZfSm4CJBOQJqqPjQACzwQAAtlm0VUo31i38D0Y0h4E",
]

#---------------STICKERS---------------#


#---------------EMOJIOS---------------#

EMOJIOS = [
    "💣",
    "💥",
    "🪄",
    "🧨",
    "⚡",
    "🤡",
    "👻",
    "🎃",
    "🎩",
    "🕊",
]


#---------------EMOJIOS---------------#

@nexichat.on_cmd(["start", "aistart"])
async def start(_, m: Message):
    if m.chat.type == ChatType.PRIVATE:
        accha = await m.reply_text(
            text=random.choice(EMOJIOS),
        )
        await asyncio.sleep(1.3)
        await accha.edit("__𝖕𝖎𝖓𝖌 𝖕𝖔𝖓𝖌 ꨄ︎ ѕтαятιиg..__")
        await asyncio.sleep(0.2)
        await accha.edit("__𝖕𝖎𝖓𝖌 𝖕𝖔𝖓𝖌 ꨄ sтαятιиg.....__")
        await asyncio.sleep(0.2)
        await accha.edit("__𝖕𝖎𝖓𝖌 𝖕𝖔𝖓𝖌 ꨄ︎ sтαятιиg..__")
        await asyncio.sleep(0.2)
        await accha.delete()
        umm = await m.reply_sticker(sticker=random.choice(STICKER))
        await asyncio.sleep(2)
        await umm.delete()
        await m.reply_text(
            text=f"""**๏ ʜᴇʏ..**\n\n**🥀ᴡᴇʟᴄᴏᴍᴇ❤ᴛᴏ💕sᴜᴘᴇʀғᴀsᴛ💗ᴀɪ🥀ᴅᴇsɪɢɴᴇᴅ🌹ᴄʜᴀᴛʙᴏᴛ🍁**"""
        )
        await add_served_user(m.from_user.id)
    else:
        await m.reply_photo(
            photo=random.choice(IMG),
            caption=START,
            reply_markup=InlineKeyboardMarkup(HELP_START),
        )
        await add_served_chat(m.chat.id)


@nexichat.on_cmd("help")
async def help(client: nexichat, m: Message):
    if m.chat.type == ChatType.PRIVATE:
        hmm = await m.reply_photo(
            photo=random.choice(IMG),
            caption=HELP_READ,
            reply_markup=InlineKeyboardMarkup(HELP_BTN),
        )
        await add_served_user(m.from_user.id)
    else:
        await m.reply_photo(
            photo=random.choice(IMG),
            caption="**ʜᴇʏ, ᴘᴍ ᴍᴇ ғᴏʀ ʜᴇʟᴘ ᴄᴏᴍᴍᴀɴᴅs!**",
            reply_markup=InlineKeyboardMarkup(HELP_BUTN),
        )
        await add_served_chat(m.chat.id)


@nexichat.on_cmd("crepo")
async def repo(_, m: Message):
    await m.reply_text(
        text=SOURCE_READ,
        reply_markup=InlineKeyboardMarkup(CLOSE_BTN),
        disable_web_page_preview=True,
    )


@nexichat.on_message(filters.new_chat_members)
async def welcome(_, m: Message):
    for member in m.new_chat_members:
        await m.reply_photo(photo=random.choice(IMG), caption=START)
