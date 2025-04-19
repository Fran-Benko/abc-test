from config.sentimentAnalyzer import OptimizedSentimentAnalyzer
from typing import Dict, List, Union

def analyze_sentiment(news_data: List[Dict], reddit_data: List[Dict]) -> Dict[str, Union[float, int]]:
    """Main function to analyze sentiment"""
    analyzer = OptimizedSentimentAnalyzer()

    # Process data
    news_metrics = analyzer.process_news(news_data)
    reddit_metrics = analyzer.process_reddit(reddit_data)

    # Combine metrics
    combined_metrics = {**news_metrics, **reddit_metrics}

    # Calculate overall sentiment if both sources are available
    if news_metrics and reddit_metrics:
        news_weight = 0.6
        reddit_weight = 0.4
        combined_metrics['overall_sentiment'] = (
            news_weight * news_metrics['news_sentiment_mean'] +
            reddit_weight * reddit_metrics['reddit_sentiment_mean']
        )

    return combined_metrics

