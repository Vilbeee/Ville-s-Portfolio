import yfinance as yf
import pandas as pd
import pyodbc

# Define the list of tickers from the S&P 100
sp100_tickers = [
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

# Function to fetch historical stock data
def fetch_historical_data(tickers):
    all_data = []

    for ticker in tickers:
        print(f"Fetching historical data for {ticker}...")
        # Fetch historical data for the last 5 years
        data = yf.download(ticker, period='5y', interval='1d')
        data['Ticker'] = ticker  # Add the ticker symbol as a column
        data.reset_index(inplace=True)  # Reset index to make 'Date' a column
        all_data.append(data)

    # Concatenate all data into a single DataFrame
    historical_data = pd.concat(all_data)
    return historical_data

# Fetch historical stock data
historical_data = fetch_historical_data(sp100_tickers)

# Prepare data for SQL Server
historical_data['Date'] = pd.to_datetime(historical_data['Date']).dt.date
historical_data['stock_value_id'] = historical_data['Ticker'] + '_' + historical_data['Date'].astype(str)

# Database connection settings
server = 'DESKTOP-HL3NT24'
database = 'Finance'
table = 's_and_p_daily_test'
connection_string = f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};Trusted_Connection=yes;'

# Insert data into SQL Server
try:
    with pyodbc.connect(connection_string) as conn:
        cursor = conn.cursor()
        for index, row in historical_data.iterrows():
            cursor.execute(f"""
                INSERT INTO {table} (stock_value_id, symbol, date, open_price, high_price, low_price, close_price, adjusted_close, volume)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)""",
                row['stock_value_id'], row['Ticker'], row['Date'], row['Open'], row['High'], row['Low'], row['Close'], row['Adj Close'], row['Volume'])
        conn.commit()
        print("Data successfully inserted into SQL Server.")
except Exception as e:
    print(f"Error inserting data: {e}")
