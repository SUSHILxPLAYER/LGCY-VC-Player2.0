import asyncio
from time import time
from datetime import datetime
from modules.helpers.filters import command
from modules.helpers.command import commandpro
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton


START_TIME = datetime.utcnow()
START_TIME_ISO = START_TIME.replace(microsecond=0).isoformat()
TIME_DURATION_UNITS = (
    ('week', 60 * 60 * 24 * 7),
    ('day', 60 * 60 * 24),
    ('hour', 60 * 60),
    ('min', 60),
    ('sec', 1)
)

async def _human_time_duration(seconds):
    if seconds == 0:
        return 'inf'
    parts = []
    for unit, div in TIME_DURATION_UNITS:
        amount, seconds = divmod(int(seconds), div)
        if amount > 0:
            parts.append('{} {}{}'
                         .format(amount, unit, "" if amount == 1 else "s"))
    return ', '.join(parts)
    
   

@Client.on_message(command("start") & filters.private & ~filters.edited)
async def start_(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/4afd7b71eebcaacb96390.jpg",
        caption=f"""**I ᴀᴍ 𝙉𝘼𝙑𝙔𝘼 𝘽𝙊𝙏
ʙᴏᴛ ʜᴀɴᴅʟᴇ ʙʏ [𝙇𝙂𝘾𝙔 𝙉𝘼𝙑𝙔𝘼 𝘿𝙄𝙎𝘾𝙐𝙎](https://t.me/NAVYA_DISCUS)**""",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        " ❰𝐆𝐫𝐨𝐮𝐩 𝐒𝐮𝐩𝐩𝐨𝐫𝐭❱ ", url=f"https://t.me/NAVYA_DISCUS")
                ]
                
           ]
        ),
    )
    
    
@Client.on_message(commandpro(["/start", "/alive", "alex", "hi", "Hi", "Hello", "hello"]) & filters.group & ~filters.edited)
async def start(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/4875ccf6172c69ecbb7c2.mp4",
        caption=f"""""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        " ❰𝐆𝐫𝐨𝐮𝐩 𝐒𝐮𝐩𝐩𝐨𝐫𝐭❱ ", url=f"https://t.me/NAVYA_DISCUS")
                ]
            ]
        ),
    )
