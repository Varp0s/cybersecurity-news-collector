from bs4 import BeautifulSoup
import feedparser
from datetime import datetime
from helper.request_helper import send_get_request, send_post_request
import os 
from dotenv import load_dotenv
from pathlib import Path

# Load environment variables
env_path = Path('./env/.env')
load_dotenv(dotenv_path=env_path)

THE_CYBERWIRE_RSS = os.getenv("THE_CYBERWIRE_RSS")

def get_threatpost_articles():
    threatpost_content = feedparser.parse(THE_CYBERWIRE_RSS)

    all_articles = []

    for security_news_threatpost in threatpost_content.entries:
        title = security_news_threatpost.title
        link = security_news_threatpost.link
        published_date = security_news_threatpost.published

        threatpost_content = send_get_request(link)
        parse_html = BeautifulSoup(threatpost_content.text, 'html.parser')
        article_content_div = parse_html.find('div', class_='c-article__content')
        article_content = article_content_div.find_all('p')
        article_content = [p.text.strip() for p in article_content if p.text.strip() not in [
            '', 'Share this article:', ' ', ' ']] 

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