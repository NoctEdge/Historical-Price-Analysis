# Historical Price Analysis
Analyze historical cryptocurrency price data to identify patterns, trends, and correlations.

**Please note that this code provides a starting point for historical price analysis. You may need to modify and enhance the code based on your specific analysis requirements, such as adding additional technical indicators, implementing advanced analysis techniques, or incorporating other visualization methods.

Before using you have the required libraries ```requests```, ```pandas```, ```matplotlib```, ```mplfinance``` installed before running the code. You can install them using the following commands:
```
pip install requests
pip install pandas
pip install matplotlib
pip install mplfinance
```

__1. Data Retrieval:__

 - The ```fetch_historical_data``` method fetches historical price data from the specified API using the ```requests``` library and stores it in the ```self.data``` variable.
   

__2. Data Analysis:__

 - The ```analyze_price_data method``` converts the data to a pandas DataFrame for analysis and manipulation.
 - Basic statistics of the price data are printed using the ```describe``` method of the DataFrame.
 - Moving averages (MA) are calculated for closing prices and added as additional columns to the DataFrame.
 - A line chart is generated using ```matplotlib``` to visualize the closing prices and moving averages.
 - A candlestick chart is generated using ```mplfinance``` to visualize the historical price data.

**To use this code, replace the ```api_url``` variable with the actual API endpoint to fetch historical price data for your desired cryptocurrency. Additionally, customize the data manipulation and analysis steps in the ```analyze_price_data``` method based on your specific requirements.
