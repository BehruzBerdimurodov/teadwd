import os
import logging
from dotenv import load_dotenv
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update, WebAppInfo
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes
load_dotenv()
TOKEN = os.getenv("BOT_TOKEN")
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):

    kb = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="salom",callback_data="salom", style='success')],
            [InlineKeyboardButton(text="salom1",callback_data="salom1", style='primary')],
            [InlineKeyboardButton(text="salom2",callback_data="salom2", style='danger')],
        ]
    )

    
    await update.message.reply_text(
        "Assalomu alaykum! Kerakli tugmani tanlang:",
        reply_markup=kb
    )

async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    
    if query.data == "salom":
        await query.message.reply_text("Swafawf")
    elif query.data == "salom1":
        await query.message.reply_text("Bwfawfawf")
    elif query.data == "salom2":
        await query.message.reply_text("awdawd")

if __name__ == '__main__':
    application = ApplicationBuilder().token(TOKEN).build()

    application.add_handler(CommandHandler('start', start))
    application.add_handler(CallbackQueryHandler(button_handler))
    print("Bot ishlamoqda...")
    application.run_polling()
