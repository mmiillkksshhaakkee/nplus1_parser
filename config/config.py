#import requests as re
import json
#response = re.get(url)
#headers = response.headers

text = "Host: nplus1.ru, \
User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:139.0) Gecko/20100101 Firefox/139.0, \
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8,\
Accept-Language: ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3,\
Accept-Encoding: gzip, deflate, br, zstd,\
Upgrade-Insecure-Requests: 1,\
Sec-Fetch-Dest: document,\
Sec-Fetch-Mode: navigate,\
Sec-Fetch-Site: none,\
Sec-Fetch-User: ?1,\
Connection: keep-alive"

items = [item.strip() for item in text.split(",")]
data = {}
for item in items:
    key, value = item.split(":", 1)
    data[key.strip()] = value.strip()

json_data = json.dumps(data, indent=4)

BASE_URL = "https://nplus1.ru"
RSS_URL = "https://nplus1.ru/rss"

HEADERS = json_data.encode('utf-8')
TIME_PERIOD = 7

OUTPUT_PATH = "data/articles.json"

TELEGRAM_TOKEN = ""
CHAT_ID = None