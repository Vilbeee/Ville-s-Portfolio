import yfinance as yf
import pandas as pd

# Define the ticker symbol for the S&P 500 index
sp500_ticker = "^GSPC"  # S&P 500 Index

# Set the start and end dates for the last 5 years
start_date = "2019-10-01"
end_date = "2024-10-01"

# Fetch the historical data for the S&P 500 index
sp500_data = yf.download(sp500_ticker, start=start_date, end=end_date)

# Reset the index to convert the date to a column
sp500_data.reset_index(inplace=True)

# Save the data to a CSV file
sp500_data.to_csv('sp500_daily_data.csv', index=False)

print("S&P 500 daily index data has been fetched and saved to 'sp500_daily_data.csv'.")
