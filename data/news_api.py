# data/news_api.py
import requests
from config.settings import FINANCIAL_NEWS_API_KEY, FINANCIAL_NEWS_API_URL

class NewsAPI:
    @staticmethod
    def get_news(ticker: str) -> str:

        lstParams = [
            FINANCIAL_NEWS_API_URL,
            FINANCIAL_NEWS_API_KEY,
            ticker
        ]
        
        newsAPIurl = "{}?apikey={}&qInTitle={}&language=en".format(lstParams)

        try:
            response = requests.get(newsAPIurl)
            response.raise_for_status()
            return response.json().get("results", [])
        except requests.exceptions.RequestException as e:
            print(f"Error fetching news: {e}")
            return []