from datetime import datetime
from sys import version_info
from time import time

from config import (
    ALIVE_IMG,
    ALIVE_NAME,
    BOT_NAME,
    BOT_USERNAME,
    GROUP_SUPPORT,
    OWNER_NAME,
    UPDATES_CHANNEL,
)
from program import __version__
from driver.filters import command, other_filters
from pyrogram import Client, filters
from pyrogram import __version__ as pyrover
from pytgcalls import (__version__ as pytover)
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message

__major__ = 0
__minor__ = 2
__micro__ = 1

__python_version__ = f"{version_info[0]}.{version_info[1]}.{version_info[2]}"


START_TIME = datetime.utcnow()
START_TIME_ISO = START_TIME.replace(microsecond=0).isoformat()
TIME_DURATION_UNITS = (
    ("week", 60 * 60 * 24 * 7),
    ("day", 60 * 60 * 24),
    ("hour", 60 * 60),
    ("min", 60),
    ("sec", 1),
)


async def _human_time_duration(seconds):
    if seconds == 0:
        return "inf"
    parts = []
    for unit, div in TIME_DURATION_UNITS:
        amount, seconds = divmod(int(seconds), div)
        if amount > 0:
            parts.append("{} {}{}".format(amount, unit, "" if amount == 1 else "s"))
    return ", ".join(parts)


@Client.on_message(
    command(["/start", f"/start@{BOT_USERNAME}"]) & filters.private & ~filters.edited
)
async def start_(client: Client, message: Message):
    await message.reply_text(
        f"""♥**اهــلايـبـنـي؟ {message.from_user.mention()} !**\n
🎗 [{BOT_NAME}](https://t.me/{BOT_USERNAME}) **مــرحـبا بـڪ انا بـوت اسـتطـيع تشـغيـل اغـانـي وفـيديـو فـي الـمـحـادثـه الصـوتـيه🍫.︙**

🥇︙ **لمعرفة استخدامي بشڪل صحيح اضغط علي زر اوامـر الـتـشـغـيل!**

🥇︙ **لـتـفـعـيلي بجروبڪ اضغط عــلـي تـفعـيل الـبوت!**
""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        " اضفني الى مجموعتك ",
                        url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
                    )
                ],
                [InlineKeyboardButton(" تفعيل البوت ", callback_data="cbhowtouse")],
                [
                    InlineKeyboardButton(" اوامر التشغيل ", callback_data="cbcmds"),
                    InlineKeyboardButton(" مالك البوت ", url=f"https://t.me/{OWNER_NAME}"),
                ],
                [
                    InlineKeyboardButton(
                        " الـدعـم", url=f"https://t.me/{GROUP_SUPPORT}"
                    ),
                    InlineKeyboardButton(
                        "قـناه الـسورس", url=f"https://t.me/{UPDATES_CHANNEL}"
                    ),
                ],
                [
                    InlineKeyboardButton(
                        "⃟✦𝗦َ𝙤𝙐𝙧𝘾𝙚َ 𝙤𝘄َ𝗦َ✦", url="https://t.me/W_EL_SO_N"
                    )
                ],
            ]
        ),
        disable_web_page_preview=True,
    )


@Client.on_message(
    command(["الحاله", f"alive@{BOT_USERNAME}"]) & filters.group & ~filters.edited
)
async def alive(client: Client, message: Message):
    current_time = datetime.utcnow()
    uptime_sec = (current_time - START_TIME).total_seconds()
    uptime = await _human_time_duration(int(uptime_sec))

    keyboard = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton("اوامر التشغيل", url=f"https://t.me/VFF35"),
                InlineKeyboardButton(
                    "الـمـطـور", url=f"https://t.me/DEV_WELSON"
                ),
            ]
        ]
    )

    alive = f"**هلا {message.from_user.mention()}, i'm {BOT_NAME}**\n\n البـوت يـعمـل بـشڪـل مـمتاز𖠀\n حٌسأّبِ أّلَمَسأّعٌدِ أّلَخَأّصٌ بِيِّ: [{ALIVE_NAME}] \n\n**شڪرا لڪ عـلي اضافـتي الان اقـوم بـتشـغيـل الموسيقي ༗** "

    await message.reply_photo(
        photo=f"{ALIVE_IMG}",
        caption=alive,
        reply_markup=keyboard,
    )

@Client.on_message(
    command(["السورس", f"SUORCE@{BOT_USERNAME}"]) & filters.group & ~filters.edited
)
async def src(client: Client, message: Message):
    current_time = datetime.utcnow()
    uptime_sec = (current_time - START_TIME).total_seconds()
    uptime = await _human_time_duration(int(uptime_sec))

    keyboard = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton("اوامر التشغيل", url=f"https://t.me/VFF35"),
                InlineKeyboardButton(
                    "مطور السورس", url=f"https://t.me/QABNADLIB"
                ),
            ]
        ]
    )

    alive = f"**هلا {message.from_user.mention()}, i'm {BOT_NAME}**\n\nℹ️ 🎶 هذا هو ويلسون المجاني\nℹ️  اختصاص هذا البوت لتشغيل مقاطع صوتية او مقاطع الفيديو في المكالمات الصوتية \n\n**⚒ لعرض اوامر البوت يمكنك مشاهده الفيديو او قم بدخول الى خاص البوت وتابع التعليمات** 💖"

    await message.reply_photo(
        photo=f"{ALIVE_IMG}",
        caption=alive,
        reply_markup=keyboard,
    )


@Client.on_message(command(["بنك", f"ping@{BOT_USERNAME}"]) & ~filters.edited)
async def ping_pong(client: Client, message: Message):
    start = time()
    m_reply = await message.reply_text("جاري الحساب...")
    delta_ping = time() - start
    await m_reply.edit_text("🏓 `اابنك!!`\n" f"⚡️ `{delta_ping * 1000:.3f} ms`")


@Client.on_message(command(["فحص", f"uptime@{BOT_USERNAME}"]) & ~filters.edited)
async def get_uptime(client: Client, message: Message):
    current_time = datetime.utcnow()
    uptime_sec = (current_time - START_TIME).total_seconds()
    uptime = await _human_time_duration(int(uptime_sec))
    await message.reply_text(
        "🤖 حاله البوت:\n"
        f"• **المدة:** `{uptime}`\n"
        f"• **وقت التشغيل:** `{START_TIME_ISO}`"
    )
