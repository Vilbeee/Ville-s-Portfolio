import yfinance as yf
import pandas as pd

# Define the list of tickers from the S&P 100 (Top 100 Large Cap Companies in the US)
sp100_tickers = [
    'AAPL', 'MSFT', 'GOOGL', 'AMZN', 'NVDA', 'BRK-B', 'META', 'TSLA', 'UNH', 'JNJ',
    'V', 'XOM', 'PG', 'LLY', 'MA', 'HD', 'CVX', 'MRK', 'ABBV', 'PEP', 'KO', 'PFE', 
    'AVGO', 'COST', 'TMO', 'MCD', 'WMT', 'CSCO', 'ACN', 'ABT', 'DHR', 'NFLX', 'LIN',
    'VZ', 'ADBE', 'NKE', 'TXN', 'CRM', 'NEE', 'PM', 'BMY', 'COP', 'QCOM', 'HON',
    'MS', 'ORCL', 'RTX', 'INTC', 'AMGN', 'SPGI', 'IBM', 'GS', 'CAT', 'BLK', 'UPS',
    'MDT', 'SCHW', 'UNP', 'DE', 'LOW', 'GILD', 'CVS', 'SBUX', 'INTU', 'NOW', 'PLD',
    'AXP', 'MO', 'BKNG', 'T', 'ISRG', 'MMC', 'EL', 'LMT', 'SYK', 'BA', 'ADP', 'MDLZ',
    'ZTS', 'GE', 'AMT', 'TMUS', 'MU', 'PYPL', 'C', 'CI', 'CB', 'APD', 'F', 'MRNA',
    'EQIX', 'ICE', 'GM', 'EW', 'DUK', 'SO', 'REGN', 'PGR', 'HUM', 'PSA', 'PLTR', 'KMB',
    'CL', 'LRCX', 'AIG'
]

# Download company information using yfinance
def get_company_info(tickers):
    company_info = {}
    for ticker in tickers:
        company = yf.Ticker(ticker)
        company_info[ticker] = company.info
    return company_info

# Example: Get info for top 100 large-cap companies
top_100_large_cap_info = get_company_info(sp100_tickers)

# Create a dataframe to display relevant details
df_large_cap = pd.DataFrame(top_100_large_cap_info).T

# Save the dataframe to an Excel file
output_file = 'Top_100_Large_Cap_Companies.xlsx'
df_large_cap[['shortName', 'marketCap', 'sector', 'industry']].to_excel(output_file, index=True)

print(f"Data has been saved to {output_file}")