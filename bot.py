print("Temesales-Bot")
from telegram.ext import Application, CommandHandler, MessageHandler, filters
import os

TOKEN = os.getenv("BOT_TOKEN")

async def start(update, context):
    await update.message.reply_text(
        "☕ እንኳን ወደ Teme Coffee AI Assistant በደህና መጡ!"
    )

async def message(update, context):
    user_text = update.message.text

    if "ቡና" in user_text or "coffee" in user_text.lower():
        reply = "☕ Teme Coffee Yirgacheffe ቡና አለን። ለማዘዝ ይንገሩን።"
    else:
        reply = "እናመሰግናለን። Teme Coffee AI Assistant እየረዳዎት ነው።"

    await update.message.reply_text(reply)


app = Application.builder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT, message))

app.run_polling()
