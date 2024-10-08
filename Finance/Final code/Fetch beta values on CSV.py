import yfinance as yf
import pandas as pd
import numpy as np  # Import numpy to use np.nan

# Define the list of S&P 500 tickers (replace with your actual tickers)
tickers = [
    'AAPL', 'MSFT', 'GOOGL', 'AMZN', 'NVDA', 'BRK-B', 'META', 'TSLA', 'UNH', 'JNJ',
    'V', 'XOM', 'PG', 'LLY', 'MA', 'HD', 'CVX', 'MRK', 'ABBV', 'PEP', 'KO', 'PFE', 
    'AVGO', 'COST', 'TMO', 'MCD', 'WMT', 'CSCO', 'ACN', 'ABT', 'DHR', 'NFLX', 'LIN',
    'VZ', 'ADBE', 'NKE', 'TXN', 'CRM', 'NEE', 'PM', 'BMY', 'COP', 'QCOM', 'HON',
    'MS', 'ORCL', 'RTX', 'INTC', 'AMGN', 'SPGI', 'IBM', 'GS', 'CAT', 'BLK', 'UPS',
    'MDT', 'SCHW', 'UNP', 'DE', 'LOW', 'GILD', 'CVS', 'SBUX', 'INTU', 'NOW', 'PLD',
    'AXP', 'MO', 'BKNG', 'T', 'ISRG', 'MMC', 'EL', 'LMT', 'SYK', 'BA', 'ADP', 'MDLZ',
    'ZTS', 'GE', 'AMT', 'TMUS', 'MU', 'PYPL', 'C', 'CI', 'CB', 'APD', 'F', 'MRNA',
    'EQIX', 'ICE', 'GM', 'EW', 'DUK', 'SO', 'REGN', 'PGR', 'HUM', 'PSA'
]

# Initialize an empty list to store the beta values
beta_values_list = []

# Fetch the beta values for each ticker
for ticker in tickers:
    print(f'Fetching beta value for {ticker}...')
    try:
        stock = yf.Ticker(ticker)
        beta = stock.info.get('beta', np.nan)  # Get beta value, default to np.nan if not available
        
        # Append the beta value to the list
        beta_values_list.append({
            'ticker': ticker,
            'beta': beta,
            'date': pd.Timestamp.now().date()  # Add the current date
        })
        
    except Exception as e:
        print(f'Error fetching data for {ticker}: {e}')

# Create a DataFrame from the list of beta values
beta_values = pd.DataFrame(beta_values_list)

# Save the DataFrame to a CSV file
beta_values.to_csv('beta_values.csv', index=False)

print('Beta values fetched and saved successfully!')
