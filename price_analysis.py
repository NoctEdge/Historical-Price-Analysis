import requests
import pandas as pd
import matplotlib.pyplot as plt
import mplfinance as mpf

class HistoricalPriceAnalyzer:
    def __init__(self, api_url, coin_symbol):
        self.api_url = api_url
        self.coin_symbol = coin_symbol
        self.data = None

    def fetch_historical_data(self):
        # Fetch historical price data from the API
        response = requests.get(self.api_url)
        if response.status_code == 200:
            self.data = response.json()
        else:
            print("Error fetching historical data from the API.")

    def analyze_price_data(self):
        # Convert data to pandas DataFrame for analysis
        df = pd.DataFrame(self.data)

        # Perform data manipulation and analysis using pandas

        # Print basic statistics
        print("Basic Statistics:")
        print(df.describe())
        print("-----------------")

        # Calculate moving averages
        df['MA10'] = df['close'].rolling(window=10).mean()
        df['MA20'] = df['close'].rolling(window=20).mean()

        # Generate line chart for closing prices and moving averages
        plt.figure(figsize=(12, 6))
        plt.plot(df['close'], label='Close')
        plt.plot(df['MA10'], label='MA10')
        plt.plot(df['MA20'], label='MA20')
        plt.title(f'{self.coin_symbol} Historical Price Analysis')
        plt.xlabel('Date')
        plt.ylabel('Price')
        plt.legend()
        plt.show()

        # Generate candlestick chart
        df['date'] = pd.to_datetime(df['date'], unit='s')
        df.set_index('date', inplace=True)
        mpf.plot(df, type='candle', title=f'{self.coin_symbol} Candlestick Chart')

# Example usage:

# Define API URL and coin symbol
api_url = "https://api.example.com/historical-data"
coin_symbol = "BTC"

# Create an instance of HistoricalPriceAnalyzer
analyzer = HistoricalPriceAnalyzer(api_url, coin_symbol)

# Fetch historical price data
analyzer.fetch_historical_data()

# Analyze and visualize price data
analyzer.analyze_price_data()
