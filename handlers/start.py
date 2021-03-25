from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton


@Client.on_message(
    filters.command("start")
    & filters.private
    & ~ filters.edited
)
async def start_(client: Client, message: Message):
    await message.reply_text(
        f"""<b>👋🏻 Hi {message.from_user.first_name}!</b>
I am eliza music robot [☺️](https://telegra.ph/file/9ae661b212ecce3ecf1a1.jpg)
.""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "SOURCE", url="https://t.me/unitedbotsupport"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "SUPPORT", url="https://t.me/unitedbotsupport"
                    ),
                    InlineKeyboardButton(
                        "CHANNEL", url="https://t.me/nimmisupport"
                    ),
                    InlineKeyboardButton(
                        "OFF TOPIC", url="https://t.me/unitedbotsupport" )
                ],
                [
                    InlineKeyboardButton(
                        "OWNER", url="https://t.me/basi_mon"
                    )
                ]
            ]
        )
    )


@Client.on_message(
    filters.command("start")
    & filters.group
    & ~ filters.edited
)
async def start(client: Client, message: Message):
    await message.reply_text(
        "SEARCH YT VIDEO",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "YES", switch_inline_query_current_chat=""
                    ),
                    InlineKeyboardButton(
                        "NO", callback_data="close"
                    )
                ]
            ]
        )
    )
