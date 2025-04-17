# data/news_api.py
import requests
from config.settings import FINANCIAL_NEWS_API_KEY, FINANCIAL_NEWS_API_URL

class NewsAPI:
    @staticmethod
    def get_news(ticker: str, start_time: str, end_time: str) -> list:
        """Fetch financial news articles for the ticker."""
        params = {
            "ticker": ticker,
            "start_time": start_time,
            "end_time": end_time,
            "api_key": FINANCIAL_NEWS_API_KEY
        }

        try:
            response = requests.get(FINANCIAL_NEWS_API_URL, params=params)
            response.raise_for_status()
            return response.json().get("articles", [])
        except requests.exceptions.RequestException as e:
            print(f"Error fetching news: {e}")
            return []