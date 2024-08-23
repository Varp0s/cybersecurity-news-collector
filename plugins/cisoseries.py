from bs4 import BeautifulSoup
import feedparser
from datetime import datetime
from helper.request_helper import send_get_request, send_get_request_cookies_headers
import os 
from dotenv import load_dotenv
from pathlib import Path
import time

# Load environment variables
env_path = Path('./env/.env')
load_dotenv(dotenv_path=env_path)

CISCOSERIES_RSS = os.getenv("CISCOSERIES_RSS")

def get_cisoseries_articles():
    cisoseries_content = feedparser.parse(CISCOSERIES_RSS)
    all_articles = []

    for security_news_cisoseries in cisoseries_content.entries:
        title = security_news_cisoseries.title
        link = security_news_cisoseries.link
        published_date = security_news_cisoseries.published

        cisoseries_news_content = send_get_request_cookies_headers(link)
        parse_html = BeautifulSoup(cisoseries_news_content.text, 'html.parser')
        article_content = parse_html.find('div', class_='td-post-content tagdiv-type')
        article_text = " ".join([p.get_text(strip=True).replace("\xa0", " ").replace("\n", " ") for p in article_content])

        while "td-post-source-tags" in article_text:
            article_text = article_text.split("td-post-source-tags")[0].strip()

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