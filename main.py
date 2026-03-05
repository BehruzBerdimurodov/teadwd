import os
import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.enums import ParseMode
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from dotenv import load_dotenv

# .env faylidan tokenni yuklash
load_dotenv()
TOKEN = os.getenv("BOT_TOKEN")

bot = Bot(token=TOKEN)
dp = Dispatcher()

kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="salom", callback_data="salom")],
        [InlineKeyboardButton(text="salom1", callback_data="salom1")],
        [InlineKeyboardButton(text="salom2", callback_data="salom2")],
    ]
)

@dp.message()
async def send_premium_emoji(message: types.Message):
    emoji_id = "6334722504107493295"

    await message.answer(
        f"Mana premium emoji: <tg-emoji emoji-id='{emoji_id}'>↩️</tg-emoji>",
        parse_mode=ParseMode.HTML,
        reply_markup=kb
    )

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
