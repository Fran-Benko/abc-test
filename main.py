# main.py
from data.news_api import NewsAPI
from data.reddit_api import RedditAPI
from data.coingecko_api import CoinGeckoAPI
from data.document_loader import DocumentLoader
from models.feature_engineering import FeatureEngineer
from models.ml_predictor import MLPredictor
from models.llm_interface import LLMInterface
from utils.helpers import validate_date, clean_ticker

def main():
    # Get user input
    ticker = input("Enter the ticker (e.g., AAPL or bitcoin): ")
    ticker = clean_ticker(ticker)

    start_time = input("Enter start time (YYYY-MM-DD): ")
    end_time = input("Enter end time (YYYY-MM-DD): ")

    if not all(validate_date(d) for d in [start_time, end_time]):
        print("Invalid date format. Please use YYYY-MM-DD.")
        return

    # Fetch data
    print("Fetching data...")
    news = NewsAPI.get_news(ticker, start_time, end_time)
    reddit_posts = RedditAPI.get_posts(ticker, start_time, end_time)
    coin_data = CoinGeckoAPI.get_coin_history(ticker)

    # Load documents
    documents_input = input("Enter file paths for documents (comma-separated, or press Enter to skip): ")
    doc_paths = [p.strip() for p in documents_input.split(",")] if documents_input else []
    docs_content = DocumentLoader.load_documents(doc_paths)

    # Process data
    print("Processing data...")
    features = FeatureEngineer.transform_data(news, reddit_posts, coin_data, docs_content)
    ml_prediction = MLPredictor.predict_trend(features)

    # Prepare and query LLM
    print("Analyzing with LLM...")
    llm_input = LLMInterface.prepare_input(news, reddit_posts, coin_data,
                                         ml_prediction, docs_content)
    trading_signal = LLMInterface.query_llm(llm_input)

    # Output results
    print("\nResults:")
    print(f"Trading Signal: {trading_signal['signal']}")
    print(f"Take Profit: {trading_signal['take_profit']}")
    print(f"Stop Loss: {trading_signal['stop_loss']}")

if __name__ == "__main__":
    main()