from plugins.cyberscoop_collector import get_cyberscoop_articles
from plugins.the_record_by_recorded_future import get_the_record_by_recorded_future_articles
from plugins.darkreading import get_darkreading_articles
from plugins.bleeping_computer import get_bleeping_computer_articles
from plugins.securityweek import get_securityweek_articles
from plugins.cisoseries import get_cisoseries_articles
from plugins.security_boulevard import get_security_boulevard_articles
from plugins.securityaffairs import get_securityaffairs_articles
from plugins.the_hacker_news import get_the_hacker_news_articles
from plugins.csoonline import get_csoonline_articles
from plugins.krebsonsecurity import get_krebsonsecurity_articles
from plugins.zdnet import get_zdnet_articles
from plugins.news_sophos import get_news_sophos_articles
from plugins.recordedfuture import get_the_record_by_recorded_future_articles
from plugins.cisa_gov_blog import get_cisa_gov_blog_articles
from plugins.kaspersky import get_kaspersky_articles
from plugins.mandiyant import get_mandiant_articles
from plugins.wired_security import get_wired_security_articles
from plugins.wired_ai import get_wired_ai_articles
from plugins.wired_business import get_wired_business_articles
from plugins.portswigger_research import get_portswigger_research_articles
from plugins.portswigger_daily_swig import get_portswigger_daily_articles

import time
import logging

logging.basicConfig(level=logging.INFO)

def start_crawling():
    while True:
        logging.info("Starting to crawling security news")
        get_cyberscoop_articles()
        get_the_record_by_recorded_future_articles()
        get_darkreading_articles()
        get_bleeping_computer_articles()
        get_securityweek_articles()
        get_cisoseries_articles()
        get_security_boulevard_articles()
        get_securityaffairs_articles()
        get_the_hacker_news_articles()
        get_csoonline_articles()
        get_krebsonsecurity_articles()
        get_zdnet_articles()
        get_news_sophos_articles()
        get_the_record_by_recorded_future_articles()
        get_cisa_gov_blog_articles()
        get_kaspersky_articles()
        get_mandiant_articles()
        get_wired_security_articles()
        get_wired_ai_articles()
        get_wired_business_articles()
        get_portswigger_research_articles()
        get_portswigger_daily_articles()

        logging.info("Finished crawling security news")
        logging.info("Sleeping for 1 hour")
        time.sleep(3600)

if __name__ == "__main__":
    start_crawling()