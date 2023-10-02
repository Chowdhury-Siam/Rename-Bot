from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from helper.utils import not_subscribed 

@Client.on_message(filters.private & filters.create(not_subscribed))
async def is_not_subscribed(client, message):
    buttons = [[ InlineKeyboardButton(text="📢Join My Channel📢", url=client.invitelink) ]]
    text = "**Sorry You are not a Member of My Channel. So Please kindly join My Channel to use me. **"
    await message.reply_text(text=text, reply_markup=InlineKeyboardMarkup(buttons))
          



