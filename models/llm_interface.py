# models/llm_interface.py
from typing import Dict, List

class LLMInterface:
    @staticmethod
    def prepare_input(news: list, reddit_posts: list, coin_data: dict,
                     ml_prediction: str, docs_content: List[str]) -> str:
        """Prepare input for LLM."""
        prompt_parts = []

        # Add news summary
        prompt_parts.append("Financial News Summary:\n")
        for article in news:
            prompt_parts.append(f"- {article.get('title', 'No title')}")

        # Add Reddit posts
        prompt_parts.append("\nReddit Posts Summary:\n")
        for post in reddit_posts:
            prompt_parts.append(f"- {post.get('title', 'No title')}")

        # Add coin data
        prompt_parts.append("\nCoin Historical Data Summary:\n")
        if coin_data.get("prices"):
            prompt_parts.append(f"Latest price: {coin_data['prices'][-1][1]}")

        # Add ML prediction and document context
        prompt_parts.append(f"\nML Trend Prediction: {ml_prediction}")
        prompt_parts.append("\nAdditional Documents Context:\n")
        for doc in docs_content:
            prompt_parts.append(f"{doc[:200]}...")

        return "\n".join(prompt_parts)

    @staticmethod
    def query_llm(prompt: str) -> Dict:
        """Query LLM with prepared input."""
        # Placeholder for actual LLM implementation
        return {
            "signal": "BUY",
            "take_profit": "5% above current price",
            "stop_loss": "3% below current price"
        }