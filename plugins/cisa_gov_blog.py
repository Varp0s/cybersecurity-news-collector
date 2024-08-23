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

CISA_GOV_BLOG_RSS = os.getenv("CISA_GOV_BLOG_RSS")

def get_cisa_gov_blog_articles():
    cisa_gov_blog_content = feedparser.parse(CISA_GOV_BLOG_RSS)
    all_articles = []

    for entry in cisa_gov_blog_content.entries:
        title = entry.title
        link = entry.link
        published_date = entry.published

        response = send_get_request(link)
        soup = BeautifulSoup(response.text, 'html.parser')
        article_paragraphs = soup.find_all('div', class_='c-field__content')
        article_text = " ".join([p.get_text(strip=True).replace("\xa0", " ").replace("\n", " ") for p in article_paragraphs])

        while "FeaturedThe" in article_text:
            article_text = article_text.split("FeaturedThe")[0].strip()
            
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
