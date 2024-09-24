import requests
from bs4 import BeautifulSoup
import logging
logging.basicConfig(
    filename='news_scraping.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def get_latest_articles(url):
    try:
        logging.info(f"Fetching latest articles from {url}")
        response = requests.get(url)
        response.raise_for_status()

        soup = BeautifulSoup(response.content, 'html.parser')
        articles = soup.find_all('div', class_="B1S3_B1__s3__widget__lSl3T widgetgap")
        for article in articles:
            headings = article.find_all('h2')
            for head in headings:
                anchor = head.find('a')
                title = anchor.text
                href = anchor['href']
                href = url + href
                logging.info(f"Title: {title}, Link: {href}")
                print(f"Title: {title}\nLink: {href}\n\n")

    except requests.exceptions.RequestException as e:
        logging.error(f"Error fetching the website: {e}")
get_latest_articles('https://www.indiatoday.in/')
