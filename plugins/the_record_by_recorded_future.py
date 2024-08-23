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

THE_RECORD_BY_RECORDED_FUTURE = os.getenv("THE_RECORD_BY_RECORDED_FUTURE")

def get_the_record_by_recorded_future_articles():
    the_record_by_recorded_future_content = feedparser.parse(THE_RECORD_BY_RECORDED_FUTURE)
    all_articles = []

    for security_news_the_record_by_recorded_future in the_record_by_recorded_future_content.entries:
        title = security_news_the_record_by_recorded_future.title
        link = security_news_the_record_by_recorded_future.link
        published_date = security_news_the_record_by_recorded_future.published

        the_record_by_recorded_future_news_content = send_get_request(link)
        parse_html = BeautifulSoup(the_record_by_recorded_future_news_content.text, 'html.parser')
        article_content = parse_html.find('span', class_='wysiwyg-parsed-content').text
        article_content = parse_html.find_all('p', class_='paragraph')
        article_text = " ".join([p.get_text(strip=True).replace("\xa0", " ").replace("\n", " ") for p in article_content])

        data_to_return = {
            "title": title,
            "link": link,
            "published_date": published_date,
            "content": article_content,
            "created_at": datetime.now(),
            "updated_at": datetime.now()
        }
        all_articles.append(data_to_return)
    return all_articles