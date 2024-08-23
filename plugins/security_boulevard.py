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

SECURITY_BOULEVARD_RSS = os.getenv("SECURITY_BOULEVARD_RSS")

def get_security_boulevard_articles():
    security_boulevard_content = feedparser.parse(SECURITY_BOULEVARD_RSS)
    all_articles = []

    for entry in security_boulevard_content.entries:
        title = entry.title
        link = entry.link
        published_date = entry.published

        response = send_get_request(link)
        soup = BeautifulSoup(response.text, 'html.parser')
        article_paragraphs = soup.find_all('div', class_='entry-content')[0].find_all('p')
        article_text = " ".join([p.get_text(strip=True).replace("\xa0", " ").replace("\n", " ") for p in article_paragraphs])

        if "*** This is a" in article_text:
            article_text = article_text.split("*** This is a")[0].strip()
        if "The post" in article_text:
            article_text = article_text.split("The post")[0].strip()

        article_data = {
            "title": title,
            "link": link,
            "published_date": published_date,
            "content": article_text,
            "created_at": datetime.now(),
            "updated_at": datetime.now()
        }
        all_articles.append(article_data)  
    return all_articles