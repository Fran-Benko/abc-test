from collections import defaultdict
from statistics import mean, stdev
from typing import Dict, List, Optional, Union
import re
from textblob import TextBlob



class OptimizedSentimentAnalyzer:
    """Optimized version of sentiment analyzer with reduced memory usage"""

    # Class-level constants
    POSITIVE_THRESHOLD = 0.1
    NEGATIVE_THRESHOLD = -0.1

    # Compile regex patterns once
    URL_PATTERN = re.compile(r'http\S+|www\S+|https\S+')
    SPECIAL_CHAR_PATTERN = re.compile(r'[^\w\s]')

    def __init__(self):
        # Initialize counters as defaultdict to avoid explicit initialization
        self.sentiment_stats = defaultdict(int)
        self.text_cache = {}  # Simple cache for processed text

    def clean_text(self, text: str) -> str:
        """Optimized text cleaning function"""
        if not isinstance(text, str) or not text.strip():
            return ''

        # Check cache first
        if text in self.text_cache:
            return self.text_cache[text]

        # Process text if not in cache
        cleaned = (
            self.URL_PATTERN.sub('', text.lower())
            .strip()
        )
        cleaned = self.SPECIAL_CHAR_PATTERN.sub('', cleaned)
        cleaned = ' '.join(cleaned.split())

        # Cache the result
        self.text_cache[text] = cleaned

        # Clear cache if it gets too large
        if len(self.text_cache) > 1000:
            self.text_cache.clear()

        return cleaned

    def get_sentiment_score(self, text: str) -> float:
        """Calculate sentiment score with minimal processing"""
        if not text:
            return 0.0

        cleaned_text = self.clean_text(text)
        if not cleaned_text:
            return 0.0

        return TextBlob(cleaned_text).sentiment.polarity

    def analyze_batch(self, texts: List[str]) -> List[float]:
        """Analyze multiple texts in batch"""
        return [self.get_sentiment_score(text) for text in texts]

    def process_news(self, news_data: List[Dict]) -> Dict[str, Union[float, int]]:
        """Process news data with minimal memory usage"""
        if not news_data:
            return {}

        # Process only required fields
        sentiments = []
        for article in news_data:
            title_sentiment = self.get_sentiment_score(article.get('title', ''))
            desc_sentiment = self.get_sentiment_score(article.get('description', ''))
            combined = (title_sentiment + desc_sentiment) / 2
            sentiments.append(combined)

        return self._calculate_metrics(sentiments, 'news')

    def process_reddit(self, reddit_data: List[Dict]) -> Dict[str, Union[float, int]]:
        """Process Reddit data with minimal memory usage"""
        if not reddit_data:
            return {}

        weighted_sentiments = []
        for comment in reddit_data:
            # Calculate base sentiment
            title_sent = self.get_sentiment_score(comment.get('title', ''))
            text_sent = self.get_sentiment_score(comment.get('selftext', ''))
            base_sentiment = (title_sent + text_sent) / 2

            # Apply weight based on upvote ratio and score
            weight = comment.get('upvote_ratio', 1.0) * (1 + comment.get('score', 0))**0.5
            weighted_sentiments.append(base_sentiment * weight)

        return self._calculate_metrics(weighted_sentiments, 'reddit')

    def _calculate_metrics(self, sentiments: List[float], source: str) -> Dict[str, Union[float, int]]:
        """Calculate metrics efficiently"""
        if not sentiments:
            return {}

        metrics = {}

        # Basic statistics
        metrics[f'{source}_sentiment_mean'] = mean(sentiments)

        try:
            metrics[f'{source}_sentiment_std'] = stdev(sentiments)
        except:
            metrics[f'{source}_sentiment_std'] = 0.0

        # Count sentiments
        pos_count = sum(1 for s in sentiments if s > self.POSITIVE_THRESHOLD)
        neg_count = sum(1 for s in sentiments if s < self.NEGATIVE_THRESHOLD)
        neu_count = len(sentiments) - pos_count - neg_count

        metrics.update({
            f'{source}_positive_count': pos_count,
            f'{source}_negative_count': neg_count,
            f'{source}_neutral_count': neu_count
        })

        return metrics

