# config/settings.py
from dotenv import load_dotenv
import os

load_dotenv()


# API Configuration
FINANCIAL_NEWS_API_KEY = os.environ['fin_news_key']
FINANCIAL_NEWS_API_URL = os.environ['fin_news_host']


REDDIT_CLIENT_ID = os.environ['reddit_client_id']
REDDIT_CLIENT_KEY = os.environ['reddit_client_key']

REDDIT_USR_GRANT_TP = os.environ['reddit_usr_grant_type']
REDDIT_USR_USERNAME = os.environ['reddit_usr_username']
REDDIT_USR_PASSWORD = os.environ['reddit_usr_password']

REDDIT_ACCESS_URL = os.environ['reddit_access_url']

REDDIT_HOST = os.environ['reddit_host']


COINGECKO_API_KEY = os.environ['coingeko_key']
COINGECKO_API_URL = os.environ['coingeko_host']




# Time formats
DATE_FORMAT = "%Y-%m-%d"

# Model Parameters
ML_FEATURES = ["news_count", "reddit_count", "trend", "avg_price", "doc_length"]