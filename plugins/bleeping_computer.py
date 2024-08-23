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

BLEEPING_COMPUTER_RSS = os.getenv("BLEEPING_COMPUTER_RSS")

def get_bleeping_computer_articles():
    bleeping_computer_content = feedparser.parse(BLEEPING_COMPUTER_RSS)
    all_articles = []

    for security_news_bleeping_computer in bleeping_computer_content.entries:
        title = security_news_bleeping_computer.title
        link = security_news_bleeping_computer.link
        published_date = security_news_bleeping_computer.published

        try:
            bleeping_computer_news_content = send_post_request(link)
            parse_html = BeautifulSoup(bleeping_computer_news_content.text, 'html.parser')
            article_body = parse_html.find('div', class_='article_section') or parse_html.find('div', class_='articleBody')

            # Remove the "Related Articles" section if it exists
            related_articles_div = parse_html.find('div', class_='cz-related-article-wrapp')
            if related_articles_div:
                related_articles_div.decompose()

            article_paragraphs = article_body.find_all('p')
            article_content = " ".join([p.get_text(strip=True).replace("\xa0", " ").replace("\n", " ") for p in article_paragraphs])

            data_to_return = {
                "title": title,
                "link": link,
                "published_date": published_date,
                "content": article_content,
                "created_at": datetime.now(),
                "updated_at": datetime.now()
            }
            all_articles.append(data_to_return)

        except Exception as e:
            print(f"An error occurred while processing the article '{title}': {e}")
            continue
    
    return all_articles
