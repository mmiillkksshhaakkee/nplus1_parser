import requests as re
from bs4 import BeautifulSoup

import feedparser
from datetime import datetime, timedelta

from config.config import RSS_URL, TIME_PERIOD


class Nplus1RSSParser:
    def __init__(self):
        self.feed_url = RSS_URL

    def parse_date(selfself, date_str: str) -> datetime: # parses the date from rss
        return datetime.strptime(date_str, '%a, %d %b %Y %H:%M:%S %z')

    def get_weekly_articles(self, days: int = TIME_PERIOD) -> list[dict]:
        feed = feedparser.parse(self.feed_url)
        articles = []
        cutoff_date = datetime.now() - timedelta(days=days)

        for entry in feed.entries:
            article_date = self.parse_date(entry.published)
            if article_date >= cutoff_date:
                articles.append({
                    "title": entry.title,
                    "link": entry.link,
                    "date": article_date.strftime("%d.%m.%Y"),
                    "summary": entry.summary
                })
        return articles
