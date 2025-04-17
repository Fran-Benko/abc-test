# llm-rag-trade-app


Tasks:
- Allow the user to define a ticker.
- Connect with a financial news API to extract the latest news of a defined ticket based on a time window.
- Connect with the Reddit API to get the last posts of a ticker based on a defined time window.
- Connect with the CoinGecko API to get the historical data of the ticker.
- Allow the user to load documents to prepare a context RAG to improve the technical analysis of a desired LLM.
- The LLM + RAG will assist the user with doubts regarding trading, patterns, technical indicators, etc.
- Transform and prepare all the data for a traditional ML model to predict the trend and future ticker price.
- The ML model should signal you to buy or sell, and the recommended take profit and stop loss in a format for an API to execute the actions.
- The app will allow you to select a trading strategy and backtest on the ticker.
- The app will allow you to connect an exchange API to execute the strategy.
