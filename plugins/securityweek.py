from bs4 import BeautifulSoup
import feedparser
from datetime import datetime
from helper.request_helper import send_get_request, send_post_request, send_get_request_cloudscraper
import os 
from dotenv import load_dotenv
from pathlib import Path

# Load environment variables
env_path = Path('./env/.env')
load_dotenv(dotenv_path=env_path)

SECURITYWEEK_FEED = os.getenv("SECURITYWEEK_FEED")

def get_securityweek_articles():
    securityweek_content = feedparser.parse(SECURITYWEEK_FEED)
    all_articles = []

    for security_news_securityweek in securityweek_content.entries:
        title = security_news_securityweek.title
        link = security_news_securityweek.link
        published_date = security_news_securityweek.published

        securityweek_news_content = send_get_request_cloudscraper(link)
        parse_html = BeautifulSoup(securityweek_news_content.text, 'html.parser')
        article_content = parse_html.find('div', class_='zox-post-body left zoxrel zox100')
        article_content = article_content.find_all('p')
        article_text = " ".join([p.get_text(strip=True).replace("\xa0", " ").replace("\n", " ") for p in article_content])

        while "Related:" in article_text:
            related_index = article_text.find("Related:")
            if related_index != -1:
                article_text = article_text[:related_index].strip()

        data_to_return = {
            "title": title,
            "link": link,
            "published_date": published_date,
            "content": article_text,
            "created_at": datetime.now(),
            "updated_at": datetime.now()
        }
        all_articles.append(data_to_return)
    return all_articles