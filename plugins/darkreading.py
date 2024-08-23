from bs4 import BeautifulSoup
import feedparser
from datetime import datetime
from helper.request_helper import send_get_request, send_get_request_cookies_headers, send_get_request_cloudscraper
import os 
from dotenv import load_dotenv
from pathlib import Path

# Load environment variables
env_path = Path('./env/.env')
load_dotenv(dotenv_path=env_path)

DARKREADING_RSS = os.getenv("DARKREADING_RSS")

def get_darkreading_articles():
    darkreading_rss_clean_text = send_get_request_cloudscraper(DARKREADING_RSS).text
    all_articles = []
    security_news_darkreading = feedparser.parse(darkreading_rss_clean_text)

    for security_news_darkreading in security_news_darkreading.entries:
        title = security_news_darkreading.title
        link = security_news_darkreading.link
        published_date = security_news_darkreading.published

        darkreading_news_content = send_get_request(link)
        parse_html = BeautifulSoup(darkreading_news_content.text, 'html.parser')
        
        # <div data-module="content" class="ContentModule-Wrapper">
        article_content = parse_html.find('div', class_='ContentModule-Wrapper').find_all('p')
        article_content_text = " ".join([p.get_text(strip=True).replace("\xa0", " ").replace("\n", " ") for p in article_content])

        data_to_return = {
            "title": title,
            "link": link,
            "published_date": published_date,
            "content": article_content_text,
            "created_at": datetime.now(),
            "updated_at": datetime.now()
        }
        all_articles.append(data_to_return)
    return all_articles

    # for security_news_darkreading in darkreading_content.entries:
    #     title = security_news_darkreading.title
    #     link = security_news_darkreading.link
    #     print(link)
    #     published_date = security_news_darkreading.published

    #     darkreading_news_content = send_get_request_cookies_headers(link)
    #     parse_html = BeautifulSoup(darkreading_news_content.text, 'html.parser')
    #     article_content = parse_html.find_all('p')
    #     article_content_text = " ".join([p.get_text(strip=True).replace("\xa0", " ").replace("\n", " ") for p in article_content])

    #     data_to_return = {
    #         "title": title,
    #         "link": link,
    #         "published_date": published_date,
    #         "content": article_content_text,
    #         "created_at": datetime.now(),
    #         "updated_at": datetime.now()
    #     }
    #     all_articles.append(data_to_return)  
    # return all_articles


