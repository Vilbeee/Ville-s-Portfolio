import yfinance as yf
import pandas as pd

# Define the list of S&P 500 tickers 
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

# Initialize empty DataFrames to store the yearly data
yearly_cash_flow_data = pd.DataFrame()
yearly_income_statement_data = pd.DataFrame()
yearly_balance_sheet_data = pd.DataFrame()

# Loop through each ticker
for ticker in tickers:
    print(f'Fetching yearly financial data for {ticker}...')
    try:
        # Fetch the yearly financial data
        cash_flow = yf.Ticker(ticker).cashflow
        income_statement = yf.Ticker(ticker).financials
        balance_sheet = yf.Ticker(ticker).balance_sheet

        # Transpose the DataFrames to have years as rows
        cash_flow = cash_flow.T
        income_statement = income_statement.T
        balance_sheet = balance_sheet.T

        # Check if there's data available
        if not cash_flow.empty:
            # Add a 'Date' column for yearly data
            cash_flow['date'] = cash_flow.index
            cash_flow['ticker'] = ticker
            
            # Reorder columns: Ticker first, then Date
            cash_flow = cash_flow[['ticker', 'date'] + [col for col in cash_flow.columns if col not in ['ticker', 'date']]]
            yearly_cash_flow_data = pd.concat([yearly_cash_flow_data, cash_flow])

        if not income_statement.empty:
            # Add a 'Date' column for yearly data
            income_statement['date'] = income_statement.index
            income_statement['ticker'] = ticker
            
            # Reorder columns: Ticker first, then Date
            income_statement = income_statement[['ticker', 'date'] + [col for col in income_statement.columns if col not in ['ticker', 'date']]]
            yearly_income_statement_data = pd.concat([yearly_income_statement_data, income_statement])

        if not balance_sheet.empty:
            # Add a 'Date' column for yearly data
            balance_sheet['date'] = balance_sheet.index
            balance_sheet['ticker'] = ticker
            
            # Reorder columns: Ticker first, then Date
            balance_sheet = balance_sheet[['ticker', 'date'] + [col for col in balance_sheet.columns if col not in ['ticker', 'date']]]
            yearly_balance_sheet_data = pd.concat([yearly_balance_sheet_data, balance_sheet])

    except Exception as e:
        print(f'Error fetching data for {ticker}: {e}')

# Reset the index
yearly_cash_flow_data.reset_index(drop=True, inplace=True)
yearly_income_statement_data.reset_index(drop=True, inplace=True)
yearly_balance_sheet_data.reset_index(drop=True, inplace=True)

# Rename columns to lower case with underscores
yearly_cash_flow_data.columns = yearly_cash_flow_data.columns.str.lower().str.replace(' ', '_')
yearly_income_statement_data.columns = yearly_income_statement_data.columns.str.lower().str.replace(' ', '_')
yearly_balance_sheet_data.columns = yearly_balance_sheet_data.columns.str.lower().str.replace(' ', '_')

# Save the DataFrames to CSV files
yearly_cash_flow_data.to_csv('yearly_cash_flow_data.csv', index=False)
yearly_income_statement_data.to_csv('yearly_income_statement_data.csv', index=False)
yearly_balance_sheet_data.to_csv('yearly_balance_sheet_data.csv', index=False)

print('Yearly financial statements fetched and saved successfully!')
