import yfinance as yf
import pandas as pd

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
    'EQIX', 'ICE', 'GM', 'EW', 'DUK', 'SO', 'REGN', 'PGR', 'HUM', 'PSA'  # Add your other tickers here
]

def fetch_financial_data(tickers):
    # Initialize empty DataFrames for each financial statement
    ttm_income_statement_data = pd.DataFrame()
    ttm_balance_sheet_data = pd.DataFrame()
    ttm_cash_flow_data = pd.DataFrame()

    # Loop through each ticker
    for ticker in tickers:
        print(f'Fetching financial data for {ticker}...')
        try:
            # Fetch quarterly income statement data
            income_statement = yf.Ticker(ticker).quarterly_financials.T
            # Check if there are at least 4 quarters of data
            if len(income_statement) >= 4:
                last_four_quarters = income_statement.head(4)
                ttm_income_data = last_four_quarters.sum()
                ttm_income_data = pd.DataFrame(ttm_income_data).T
                ttm_income_data['date'] = 'TTM 2024-10-01'
                ttm_income_data['ticker'] = ticker
                ttm_income_statement_data = pd.concat([ttm_income_statement_data, ttm_income_data])

                for index, row in last_four_quarters.iterrows():
                    row_data = pd.DataFrame(row).T
                    row_data['date'] = index
                    row_data['ticker'] = ticker
                    ttm_income_statement_data = pd.concat([ttm_income_statement_data, row_data])
            else:
                print(f'Not enough quarterly income statement data for {ticker}.')

            # Fetch quarterly balance sheet data
            balance_sheet = yf.Ticker(ticker).quarterly_balance_sheet.T
            if len(balance_sheet) >= 4:
                last_four_quarters = balance_sheet.head(4)
                ttm_balance_data = last_four_quarters.sum()
                ttm_balance_data = pd.DataFrame(ttm_balance_data).T
                ttm_balance_data['date'] = 'TTM 2024-10-01'
                ttm_balance_data['ticker'] = ticker
                ttm_balance_sheet_data = pd.concat([ttm_balance_sheet_data, ttm_balance_data])

                for index, row in last_four_quarters.iterrows():
                    row_data = pd.DataFrame(row).T
                    row_data['date'] = index
                    row_data['ticker'] = ticker
                    ttm_balance_sheet_data = pd.concat([ttm_balance_sheet_data, row_data])
            else:
                print(f'Not enough quarterly balance sheet data for {ticker}.')

            # Fetch quarterly cash flow data
            cash_flow = yf.Ticker(ticker).quarterly_cashflow.T
            if len(cash_flow) >= 4:
                last_four_quarters = cash_flow.head(4)
                ttm_cash_data = last_four_quarters.sum()
                ttm_cash_data = pd.DataFrame(ttm_cash_data).T
                ttm_cash_data['date'] = 'TTM 2024-10-01'
                ttm_cash_data['ticker'] = ticker
                ttm_cash_flow_data = pd.concat([ttm_cash_flow_data, ttm_cash_data])

                for index, row in last_four_quarters.iterrows():
                    row_data = pd.DataFrame(row).T
                    row_data['date'] = index
                    row_data['ticker'] = ticker
                    ttm_cash_flow_data = pd.concat([ttm_cash_flow_data, row_data])
            else:
                print(f'Not enough quarterly cash flow data for {ticker}.')

        except Exception as e:
            print(f'Error fetching data for {ticker}: {e}')

    # Reset the indexes and reorder columns
    for df, filename in zip([ttm_income_statement_data, ttm_balance_sheet_data, ttm_cash_flow_data],
                            ['ttm_income_statement_data.csv', 'ttm_balance_sheet_data.csv', 'ttm_cash_flow_data.csv']):
        df.reset_index(drop=True, inplace=True)
        # Reorder columns: Ticker first, then Date
        column_order = ['ticker', 'date'] + [col for col in df.columns if col not in ['ticker', 'date']]
        df = df[column_order]
        # Rename columns to lower case with underscores
        df.columns = df.columns.str.lower().str.replace(' ', '_')

        # Save each DataFrame to a separate CSV file
        df.to_csv(filename, index=False)
        print(f'{filename} saved successfully!')

# Call the function to fetch financial data
fetch_financial_data(tickers)
