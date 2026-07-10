from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo
from telegram.ext import Application, CommandHandler, ContextTypes

TOKEN = "8878314582:AAFSjgZoRbH3-d4eDg-aQFJbIlxYaI8eYOo"


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):

    keyboard = [
        [
            InlineKeyboardButton(
                "🚀 Open Calculator",
                web_app=WebAppInfo(
                    url="https://smartpercentegecalculator.netlify.app/"
                )
            )
        ]
    ]

    await update.message.reply_text(
        "📊 Smart Percentage Calculator\n\nTap below to open:",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )


app = Application.builder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))

app.run_polling()