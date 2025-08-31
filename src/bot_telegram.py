import telegram
from telegram.ext import Application, CommandHandler
from config.config import TELEGRAM_TOKEN, CHAT_ID
from src.storage import  load_from_json

class TelegramNotifier:
    def __init__(self):
        self.bot = telegram.Bot(token=TELEGRAM_TOKEN)

    async def on_message(self, article: dict):
        message = (
            f"{article['title']}**\n"
            f"{article['date']}\n"
            f"{article['link']}\n"
        )
        await self.bot.send_message(
            chat_id=CHAT_ID,
            text=message,
            parse_mode=telegram.ParseMode.MARKDOWN
        )

    async def last_article(self, update, context):
        articles = load_from_json()
        if articles:
            await self.on_message(articles[0])
        else:
            await update.message.reply_text("There's no articles.")


    async def start(self, update, context):
        global CHAT_ID
        CHAT_ID = update.effective_chat.id
        await update.message.reply_text("Bot is now active! Get ready for new articles...")

    def run(self):
        application = Application.builder().token(TELEGRAM_TOKEN).build()
        application.add_handler(CommandHandler("start", self.start))
        application.add_handler(CommandHandler("last_article", self.last_article))
        application.run_polling()