# config/settings.py
from dotenv import load_dotenv
import os

load_dotenv()


# API Configuration
FINANCIAL_NEWS_API_KEY = os.environ['fin_news_key']
FINANCIAL_NEWS_API_URL = os.environ['fin_news_host']

REDDIT_API_KEY = os.environ['reddit_key']
REDDIT_API_URL = os.environ['reddit_host']

COINGECKO_API_KEY = os.environ['coingeko_key']
COINGECKO_API_URL = os.environ['coingeko_host']




# Time formats
DATE_FORMAT = "%Y-%m-%d"

# Model Parameters
ML_FEATURES = ["news_count", "reddit_count", "trend", "avg_price", "doc_length"]