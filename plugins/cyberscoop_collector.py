from bs4 import BeautifulSoup
import feedparser
from datetime import datetime, timedelta
from helper.request_helper import send_get_request
import os 
from dotenv import load_dotenv
from pathlib import Path

# Load environment variables
env_path = Path('./env/.env')
load_dotenv(dotenv_path=env_path)

CYBERSCOOP_RSS_URL = os.getenv("CYBERSCOOP_FEED")

def get_cyberscoop_articles():
    cyberscoop_content = feedparser.parse(CYBERSCOOP_RSS_URL)
    all_articles = []

    for security_news_cyberscoop in cyberscoop_content.entries:
        title = security_news_cyberscoop.title
        link = security_news_cyberscoop.link
        published_date = security_news_cyberscoop.published

        cyberscoop_news_content = send_get_request(link)
        parse_html = BeautifulSoup(cyberscoop_news_content.text, 'html.parser')
        article_content = parse_html.find('div', class_='single-article__content').text
        article_content = parse_html.find_all('p')
        article_text = " ".join([p.get_text(strip=True).replace("\xa0", " ").replace("\n", " ") for p in article_content])

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
