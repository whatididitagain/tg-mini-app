from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackContext

# Команда /start
async def start(update: Update, context: CallbackContext):
    keyboard = [
        [InlineKeyboardButton("Запустить мини-игру", web_app="https://your-mini-app-url.com")]  # Замените URL на свой
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(
        "Привет! Нажмите на кнопку ниже, чтобы запустить мини-игру.",
        reply_markup=reply_markup
    )

if __name__ == "__main__":
    app = ApplicationBuilder().token("7451606725:AAH-5F5Cw86gDlhqD6byu1Iq4np2omu9e2w").build()

    app.add_handler(CommandHandler("start", start))

    print("Бот запущен...")
    app.run_polling()
