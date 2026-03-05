import os
import asyncio
import logging
from aiogram import Bot, Dispatcher, F, types
from aiogram.filters import Command
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo
from dotenv import load_dotenv

# .env faylidagi ma'lumotlarni yuklash
load_dotenv()

# Tokenni .env faylidan olish
TOKEN = os.getenv("BOT_TOKEN")

# Agar token xato yozilgan bo'lsa yoki topilmasa, kodni to'xtatish
if not TOKEN:
    raise ValueError("BOT_TOKEN .env faylidan topilmadi! Iltimos, tekshirib ko'ring.")

# Bot va Dispatcher obyektlari
bot = Bot(token=TOKEN)
dp = Dispatcher()

# /start komandasi uchun handler
@dp.message(Command("start"))
async def start_handler(message: types.Message):
    kb = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(
                text="🌐 Mini App ni ochish", 
                web_app=WebAppInfo(url="https://example.com") # Mini App URL'i
            )],
            [InlineKeyboardButton(text="👋 Salom", callback_data="salom")],
            [InlineKeyboardButton(text="📝 Ko'proq ma'lumot 1", callback_data="salom1")],
            [InlineKeyboardButton(text="⚠️ Ogohlantirish 2", callback_data="salom2")],
        ]
    )
    
    await message.answer(
        f"Assalomu alaykum, {message.from_user.first_name}! 🤖\n\n"
        f"Men sizning botingizman. Quyidagi tugmalardan birini tanlang "
        f"yoki Mini App ni oching:",
        reply_markup=kb
    )

# "salom" tugmasi bosilganda
@dp.callback_query(F.data == "salom")
async def process_salom(callback: types.CallbackQuery):
    await callback.message.answer("Salom! Qandaysiz? Bu uzun textlar va suhbatlar uchun birinchi javob. 😊")
    await callback.answer()

# "salom1" tugmasi bosilganda
@dp.callback_query(F.data == "salom1")
async def process_salom1(callback: types.CallbackQuery):
    await callback.message.answer(
        "Siz 'Ko'proq ma'lumot 1' tugmasini bosdingiz!\n\n"
        "Bu yerda juda ko'p ma'lumotlar yozilishi mumkin. "
        "Bot siz bilan turli mavzularda gaplashishga tayyor."
    )
    await callback.answer()

# "salom2" tugmasi bosilganda
@dp.callback_query(F.data == "salom2")
async def process_salom2(callback: types.CallbackQuery):
    await callback.message.answer(
        "Diqqat! Bu xuddi siz xohlagan 'danger' (xavfli/ogohlantiruvchi) holat uchun javob matni. 🚨"
    )
    await callback.answer()

# Asosiy ishga tushirish funksiyasi
async def main():
    logging.basicConfig(level=logging.INFO)
    print("Bot ishga tushdi...")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
