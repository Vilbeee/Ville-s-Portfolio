import yfinance as yf
import pandas as pd

# Define the tickers and time period
tickers = ['AAPL', 'MSFT', 'GOOGL', 'AMZN', 'NVDA', 'BRK-B', 'META', 'TSLA', 'UNH', 'JNJ',
    'V', 'XOM', 'PG', 'LLY', 'MA', 'HD', 'CVX', 'MRK', 'ABBV', 'PEP', 'KO', 'PFE', 
    'AVGO', 'COST', 'TMO', 'MCD', 'WMT', 'CSCO', 'ACN', 'ABT', 'DHR', 'NFLX', 'LIN',
    'VZ', 'ADBE', 'NKE', 'TXN', 'CRM', 'NEE', 'PM', 'BMY', 'COP', 'QCOM', 'HON',
    'MS', 'ORCL', 'RTX', 'INTC', 'AMGN', 'SPGI', 'IBM', 'GS', 'CAT', 'BLK', 'UPS',
    'MDT', 'SCHW', 'UNP', 'DE', 'LOW', 'GILD', 'CVS', 'SBUX', 'INTU', 'NOW', 'PLD',
    'AXP', 'MO', 'BKNG', 'T', 'ISRG', 'MMC', 'EL', 'LMT', 'SYK', 'BA', 'ADP', 'MDLZ',
    'ZTS', 'GE', 'AMT', 'TMUS', 'MU', 'PYPL', 'C', 'CI', 'CB', 'APD', 'F', 'MRNA',
    'EQIX', 'ICE', 'GM', 'EW', 'DUK', 'SO', 'REGN', 'PGR', 'HUM', 'PSA']  
start_date = "2019-10-01"
end_date = "2024-10-01"

# Initialize an empty DataFrame for the combined data
combined_data = pd.DataFrame()

# Loop over each ticker to fetch the data and calculate TTM dividend yield
for ticker_symbol in tickers:
    # Fetch historical stock data
    stock_data = yf.download(ticker_symbol, start=start_date, end=end_date, interval="1d")

    # Fetch dividend data
    stock = yf.Ticker(ticker_symbol)
    dividends = stock.dividends[start_date:end_date]

    # Convert dividends data to a DataFrame and remove timezone info
    dividends_df = dividends.reset_index()
    dividends_df.columns = ['Date', 'Dividends']
    dividends_df['Date'] = pd.to_datetime(dividends_df['Date']).dt.tz_localize(None)

    # Remove timezone info from stock data
    stock_data.reset_index(inplace=True)
    stock_data['Date'] = stock_data['Date'].dt.tz_localize(None)

    # Merge stock data with dividends data
    merged_data = pd.merge(stock_data, dividends_df, on='Date', how='left')
    merged_data['Dividends'].fillna(0, inplace=True)

    # Calculate TTM dividends over a 12-month period
    merged_data['TTM Dividends'] = (
        merged_data.set_index('Date')['Dividends']
        .rolling(window='365D', min_periods=1)
        .sum()
        .reset_index(drop=True)
    )

    # Calculate TTM dividend yield
    merged_data['forward_dividend_yield'] = (merged_data['TTM Dividends'] / merged_data['Adj Close']) * 100

    # Add ticker column to identify the ticker symbol
    merged_data['Ticker'] = ticker_symbol

    # Append the relevant columns to the combined DataFrame
    combined_data = pd.concat([combined_data, merged_data[['Date', 'Ticker', 'forward_dividend_yield']]])

# Rename columns to lower case and replace spaces with underscores
combined_data.columns = [col.lower().replace(' ', '_') for col in combined_data.columns]

# Save the combined data to a single CSV file
combined_data.to_csv('forward_dividend_yield.csv', index=False)
print("TTM dividend yield data for all tickers has been fetched and saved to 'forward_dividend_yield.csv'.")
