from datetime import datetime

def filter_by_keyword(articles: list[dict], keyword: str) -> list[dict]:
    return [
        article for article in articles
        if keyword.lower() in article["title"].lower()
        or keyword.lower() in article.get("summary", "").lower()
    ]