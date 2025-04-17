# data/reddit_api.py
import requests
from config.settings import REDDIT_API_URL

class RedditAPI:
    @staticmethod
    def get_posts(ticker: str, start_time: str, end_time: str) -> list:
        """Fetch Reddit posts mentioning the ticker."""
        params = {
            "q": ticker,
            "after": start_time,
            "before": end_time,
            "size": 50
        }

        try:
            response = requests.get(REDDIT_API_URL, params=params)
            response.raise_for_status()
            return response.json().get("data", [])
        except requests.exceptions.RequestException as e:
            print(f"Error fetching Reddit posts: {e}")
            return []