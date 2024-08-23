import requests
import cloudscraper
import time


def send_get_request(URL):
    response = requests.get(URL)
    return response

def send_post_request(URL):
    request_headers= {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36", "Content-Type": "application/x-www-form-urlencoded"}
    response= requests.post(URL, headers=request_headers)    
    return response

def send_get_request_cloudscraper(URL):
    cloudscraper_scraper= cloudscraper.create_scraper(
    browser={
        'browser': 'firefox',
        'user_agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome',
        'platform': 'windows',
        'mobile': False })

    response= cloudscraper_scraper.get(URL)
    time.sleep(5)
    return response

def send_post_request_cloudscraper(URL):
    cloudscraper_scraper= cloudscraper.create_scraper(
    browser={
        'browser': 'firefox',
        'user_agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome',
        'platform': 'windows',
        'javascript': True,
        'mobile': False, })

    response= cloudscraper_scraper.post(URL)
    return response

cookies = {
    'sucuri_cloudproxy_uuid_3e6231bc6': 'b8d5224003f331a7bda181dcebd6d129',
}

headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'tr,en;q=0.9,en-GB;q=0.8,en-US;q=0.7,ar;q=0.6',
    'cache-control': 'max-age=0',
    # 'cookie': 'sucuri_cloudproxy_uuid_3e6231bc6=b8d5224003f331a7bda181dcebd6d129',
    'dnt': '1',
    'priority': 'u=0, i',
    'sec-ch-ua': '"Not)A;Brand";v="99", "Microsoft Edge";v="127", "Chromium";v="127"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'none',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0',
}

def send_get_request_cookies_headers(URL):
    response = requests.get(URL, cookies=cookies, headers=headers)
    return response