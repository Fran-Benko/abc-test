# models/ml_predictor.py
from typing import Dict

class MLPredictor:
    @staticmethod
    def predict_trend(features: Dict) -> str:
        """Predict trend based on features."""
        if features["trend"] > 0 and features["news_count"] > features["reddit_count"]:
            return "UP"
        return "DOWN"