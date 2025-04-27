# news_post_itmedia.py
import feedparser
import requests
import logging

# ——— 設定項目 ———
RSS_URL     = "https://rss.itmedia.co.jp/rss/2.0/aiplus.xml"  # ITmedia AI＋用
WEBHOOK_URL = "https://hooks.slack.com/services/XXX/YYY/ZZZ"

MAX_ITEMS   = 5
# —————————————————

logging.basicConfig(
    filename="newsbot_itmedia.log",
    level=logging.INFO,
    format="%(asctime)s %(levelname)s: %(message)s"
)

def fetch_headlines(url, max_items=5):
    # RSSをパース
    feed = feedparser.parse(url)
    headlines = []
    for entry in feed.entries[:max_items]:
        headlines.append(f"• <{entry.link}|{entry.title}>")
    return headlines

def post_to_slack(lines):
    text = "*🌅 今朝のITmedia AI＋ヘッドライン* \n" + "\n".join(lines)
    resp = requests.post(WEBHOOK_URL, json={"text": text})
    resp.raise_for_status()
    return resp

if __name__ == "__main__":
    try:
        items = fetch_headlines(RSS_URL, MAX_ITEMS)
        if not items:
            logging.warning("取得した記事がありませんでした。")
        else:
            resp = post_to_slack(items)
            logging.info(f"Slack投稿成功：HTTP {resp.status_code}")
    except Exception as e:
        logging.error(f"エラー発生：{e}")
