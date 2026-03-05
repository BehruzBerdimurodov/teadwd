import os
import asyncio
from aiogram import Bot, Dispatcher, F, types
from aiogram.filters import Command
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo
from dotenv import load_dotenv

# .env faylidan tokenni yuklash
load_dotenv()
TOKEN = os.getenv("BOT_TOKEN")

bot = Bot(token=TOKEN)
dp = Dispatcher()
       
# Siz so'ragan tugmalar strukturasi (Mini App qo'shilgan holda)
kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="🚀 Mini App-ni ochish", web_app=WebAppInfo(url="https://google.com"))],
        [InlineKeyboardButton(text="salom",callback_data="salom", style='success')],
        [InlineKeyboardButton(text="salom1",callback_data="salom1", style='primary')],
        [InlineKeyboardButton(text="salom2",callback_data="salom2", style='danger')],
    ]
)


@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer(
        f"Salom {message.from_user.full_name}! 👋\n\n"
        "Bu ko'plab matnlar bilan ishlaydigan bot testi. "
        "Pastdagi tugmalar orqali turli xil javoblarni olishingiz mumkin.",
        reply_markup=kb
    )

@dp.callback_query(F.data == "salom")
async def callbacks_salom(callback: types.CallbackQuery):
    await callback.message.answer("Sizga ham katta salom! Bu birinchi matnli xabarimiz. 😊")
    await callback.answer()

@dp.callback_query(F.data == "salom1")
async def callbacks_salom1(callback: types.CallbackQuery):
    text = (
        "Bu juda uzun matn bo'lishi mumkin:\n"
        "1. Birinchi qator ma'lumot.\n"
        "2. Ikkinchi qator ma'lumot.\n"
        "3. Uchinchi qator ma'lumot.\n"
        "Botimiz har qanday hajmdagi matnni yubora oladi!"
    )
    await callback.message.answer(text)
    await callback.answer()

@dp.callback_query(F.data == "salom2")
async def callbacks_salom2(callback: types.CallbackQuery):
    await callback.message.answer("Bu oxirgi tugma uchun tayyorlangan maxsus javob. 🤖")
    await callback.answer()

async def main():
    print("Bot ishga tushdi...")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
