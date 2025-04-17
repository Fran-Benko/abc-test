# data/coingecko_api.py
import requests
from config.settings import COINGECKO_API_URL
from dotenv import load_dotenv
import os




class CoinGeckoAPI:
    @staticmethod
    def get_coin_history(ticker: str, days: int = 30) -> dict:

        load_dotenv()

        xRapidKey = os.environ['coingeko-key']
        xRapidHost = os.environ['coingeko-host']

        headers = {
            'x-rapidapi-key': xRapidKey,
            'x-rapidapi-host': xRapidHost
        }

        """Fetch historical market data for the ticker."""
        url = f"{COINGECKO_API_URL}/coins/{ticker}/market_chart"
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