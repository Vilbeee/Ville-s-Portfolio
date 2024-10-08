import yfinance as yf
import pandas as pd

# Define the tickers and the time period
tickers = ['AAPL', 'MSFT', 'GOOGL', 'AMZN', 'NVDA', 'BRK-B', 'META', 'TSLA', 'UNH', 'JNJ',
    'V', 'XOM', 'PG', 'LLY', 'MA', 'HD', 'CVX', 'MRK', 'ABBV', 'PEP', 'KO', 'PFE', 
    'AVGO', 'COST', 'TMO', 'MCD', 'WMT', 'CSCO', 'ACN', 'ABT', 'DHR', 'NFLX', 'LIN',
    'VZ', 'ADBE', 'NKE', 'TXN', 'CRM', 'NEE', 'PM', 'BMY', 'COP', 'QCOM', 'HON',
    'MS', 'ORCL', 'RTX', 'INTC', 'AMGN', 'SPGI', 'IBM', 'GS', 'CAT', 'BLK', 'UPS',
    'MDT', 'SCHW', 'UNP', 'DE', 'LOW', 'GILD', 'CVS', 'SBUX', 'INTU', 'NOW', 'PLD',
    'AXP', 'MO', 'BKNG', 'T', 'ISRG', 'MMC', 'EL', 'LMT', 'SYK', 'BA', 'ADP', 'MDLZ',
    'ZTS', 'GE', 'AMT', 'TMUS', 'MU', 'PYPL', 'C', 'CI', 'CB', 'APD', 'F', 'MRNA',
    'EQIX', 'ICE', 'GM', 'EW', 'DUK', 'SO', 'REGN', 'PGR', 'HUM', 'PSA']
start_date = "2019-10-01"  # 5 years ago from today
end_date = "2024-10-01"    # Today's date

# Initialize an empty DataFrame for the combined data
combined_dividends = pd.DataFrame()

# Loop over each ticker to fetch the dividend data
for ticker_symbol in tickers:
    # Fetch dividend data directly using the dividends method
    stock = yf.Ticker(ticker_symbol)
    dividends = stock.dividends[start_date:end_date]

    # Reset the index to convert the date to a column
    daily_dividends = dividends.reset_index()

    # Rename the columns
    daily_dividends.columns = ['Date', 'Dividend']

    # Add the ticker symbol to the DataFrame
    daily_dividends['Ticker'] = ticker_symbol

    # Append the data to the combined DataFrame
    combined_dividends = pd.concat([combined_dividends, daily_dividends], ignore_index=True)

# Save to a CSV file
combined_dividends.to_csv('dividends.csv', index=False)

print("Dividends have been fetched and saved to 'dividends.csv'.")
