from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = '7326231282:AAEnRs_eL8kCeWOyUoIjeOu3bWkpta32ryU'
LANDING_PAGE_URL = 'https://easy-spoons-fix.loca.lt'


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Привет! Это стартовое сообщение.')

async def play(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [[InlineKeyboardButton("Начать игру", url=LANDING_PAGE_URL)]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text('Игра началась! Нажмите кнопку ниже, чтобы открыть игру:', reply_markup=reply_markup)

if __name__ == '__main__':
    app = ApplicationBuilder().token(TOKEN).build()

    start_handler = CommandHandler('start', start)
    play_handler = CommandHandler('play', play)

    app.add_handler(start_handler)
    app.add_handler(play_handler)

    print("Bot is running...")
    app.run_polling()