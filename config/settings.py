# config/settings.py

# API Configuration
FINANCIAL_NEWS_API_KEY = "YOUR_FINANCIAL_NEWS_API_KEY"
FINANCIAL_NEWS_API_URL = "https://financialnewsapi.com/api/v1/news"
REDDIT_API_URL = "https://api.pushshift.io/reddit/search/submission/"
COINGECKO_API_URL = "https://coingecko.p.rapidapi.com"

# Time formats
DATE_FORMAT = "%Y-%m-%d"

# Model Parameters
ML_FEATURES = ["news_count", "reddit_count", "trend", "avg_price", "doc_length"]