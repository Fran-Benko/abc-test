# data/coingecko_api.py
import requests
from config.settings import COINGECKO_API_URL, COINGECKO_API_KEY




class CoinGeckoAPI:
    @staticmethod
    def get_coin_history(ticker: str, days: int = 10) -> dict:


        headers = {
            'x-rapidapi-key': COINGECKO_API_KEY,
            'x-rapidapi-host': COINGECKO_API_URL
        }

        """Fetch historical market data for the ticker."""
        url = f"https://{COINGECKO_API_URL}/coins/{ticker}/market_chart"
        params = {
            "vs_currency": "usd",
            "days": days
        }

        try:
            response = requests.get(url, headers=headers, params=params)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error fetching coin history: {e}")
            return {}