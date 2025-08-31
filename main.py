from config.config import OUTPUT_PATH
from src.main_parser import Nplus1RSSParser
from src.storage import save_to_json
from src.filters import filter_by_keyword
from src.bot_telegram import TelegramNotifier
import asyncio

async def main():
    # Parsing
    parser = Nplus1RSSParser()
    articles = parser.get_weekly_articles()

    if articles:
        filtered_articles = filter_by_keyword(articles, "физика")
        print(f"Found {len(articles)} articles for this week:")
        for a in articles[:5]:
            print(f"- {a['title']} ({a['date']})")
        #Saving the list of articles
        save_to_json(articles)
        print(f"List saved to {OUTPUT_PATH}")

        #notifying via telegram
        notifier = TelegramNotifier()
        for a in articles:
            await notifier.on_message(a)
    else:
        print("Couldn't find any articles for this week.")

if __name__ == '__main__':
    main()
