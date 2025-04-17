# models/feature_engineering.py
import pandas as pd
from typing import Dict, List

class FeatureEngineer:
    @staticmethod
    def transform_data(news: list, reddit_posts: list,
                      coin_data: dict, docs_content: List[str]) -> Dict:
        """Transform raw data into features for ML model."""
        features = {
            "news_count": len(news),
            "reddit_count": len(reddit_posts),
            "trend": 0,
            "avg_price": 0,
            "doc_length": sum(len(doc) for doc in docs_content)
        }

        # Process coin prices if available
        coin_prices = coin_data.get("prices", [])
        if coin_prices:
            df_prices = pd.DataFrame(coin_prices, columns=["timestamp", "price"])
            features["trend"] = df_prices["price"].iloc[-1] - df_prices["price"].iloc[0]
            features["avg_price"] = df_prices["price"].mean()

        return features