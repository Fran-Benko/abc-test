# utils/helpers.py
from datetime import datetime
from config.settings import DATE_FORMAT

def validate_date(date_string: str) -> bool:
    """Validate date string format."""
    try:
        datetime.strptime(date_string, DATE_FORMAT)
        return True
    except ValueError:
        return False

def clean_ticker(ticker: str) -> str:
    """Clean and validate ticker symbol."""
    return ticker.strip().lower()