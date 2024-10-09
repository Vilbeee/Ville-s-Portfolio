# [S&P500: Stock Data Cleaning & Dashboard Creation]

This is a project I did with the intention of creating a Power BI dashboard, useful for quick and easy comparison of stock data.

### Why this project?

One common problem I have faced at the beginning of my investing career is the fact that there are so many different companies and industries to choose from. In addition, for all of the singular companies, there is so much information to dig through. I always wanted to have a way to quickly weed out the bad stocks from the good ones before I begin to dive deeper into the individual companies.

As I recently graduated with a master's degree in economics, I wanted to create a project, which would showcase my skills with different data analysis programs such as SQL, Excel and PowerBI. In addition, working with stock data correlates to my personal interests regarding investing and it also showcases my ability to read and understand companies' financial statements. This is why I thought that the creation of a dashboard where you can quickly compare any amount of stocks of your own choosing, would be extremely fitting.

### Steps followed

* Step 1: Fetch data using Python with the help of ChatGPT

All of the Python codes for fetching data can be found on:

https://github.com/Vilbeee/Ville-s-Portfolio/tree/6855ca1843cf14598de0948fd742e5d2d13775d4/S%26P500%20Project/Code

Example 1: Fetching companies' information

```python
import yfinance as yf
import pandas as pd

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
```

Example 2: Fetching Beta values

```python
import yfinance as yf
import pandas as pd
import numpy as np  

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
```

* Step 2: Take the data into Excel for preliminary cleaning and to check that the data is correct. Upload data into an SQL server.


Example 1: Replacing NULL with null in Power Query

![Replacing NULL with null](https://github.com/user-attachments/assets/e2ca0775-18a2-49f9-aa35-d77018b5d3e2)

Example 2: Creating table in SQL queries and fetching data straight into my server

```SQL
CREATE TABLE s_and_p_daily_test
(
stock_value_id VARCHAR(255) NOT NULL,
symbol VARCHAR(15) NOT NULL, 
date DATE NOT NULL,
open_price DECIMAL(38, 2),
high_price DECIMAL(38, 2),
low_price DECIMAL(38, 2),
close_price DECIMAL(38, 2),
adjusted_close DECIMAL(38, 2),
volume INTEGER,
CONSTRAINT pk_s_and_p_daily_test
	PRIMARY KEY (stock_value_id)
)
```
```python
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
```

* Step 3: Use SQL queries to further clean the data and calculate financial KPIs

All of the SQL queries used in the project can be found on:

https://github.com/Vilbeee/Ville-s-Portfolio/tree/548b9ba9b3ac410ff56bd86ebc447941b7286222/S%26P500%20Project/SLQ%20Queries

Example 1: Extracting TTM from Quarterly data table. Python calculated TTM using the quarterly data.

```SQL
SELECT *
INTO ttm_cash_flow
FROM cash_flows_ttm_and_quarter
WHERE date = 'TTM 2024-10-01';
```
```SQL
DELETE FROM ttm_cash_flow_and_quarter
WHERE date = 'TTM 2024-10-01';
```
![Save quarterly tables from SQL to CSV](https://github.com/user-attachments/assets/4c7806d3-2631-4133-a333-5e97795353bf)


Example 2: Using JOIN to calculate P/E-Ratio.

```SQL
SELECT sp.date, 
ist.ticker, 
sp.adjusted_close/ist.diluted_eps pe_ratio
FROM income_statement_ttm ist
JOIN s_and_p_daily sp
ON ist.ticker = sp.symbol
WHERE sp.date = '2024-09-30';
```

Example 3: Using JOIN with aggregation to calculate ROE. Grouping by tickers and ordering by ROE.

```SQL
SELECT bsq.ticker, 
AVG(stockholders_equity) average_stockholders_equity, 
MAX(net_income)/AVG(stockholders_equity)*100 ROE
FROM balance_sheet_quarter bsq
JOIN income_statement_ttm ist
ON bsq.ticker = ist.ticker
GROUP BY bsq.ticker
ORDER BY ROE DESC;
```
Example 4: Calculating D/E-ratio using WHERE and BETWEEN to get the most recent quarterly data

```SQL
SELECT ticker, total_debt, stockholders_equity, total_debt/stockholders_equity de_ratio
FROM balance_sheet_quarter
WHERE date BETWEEN '2024-05-31' AND '2024-07-31';
```

* Step 4: Move data to PowerBI and make sure the datatypes and NULL values are correct

Example 1: This image is from Excel Power Query, but it showcases common problems in the transition from SQL to Power BI. Saving files as CSV can lead to headers not being saved, unless a setting is toggled on. The nulls are in the form of "NULL" and Power Query doesn't detect them. Data type needs to be detected after all of these problems have been taken care of.

![Detecting the right data type](https://github.com/user-attachments/assets/f33cc5ae-7601-454e-8bee-b33d2dab3398)

* Step 5: Create a dashboard in PowerBI

All of the DAX codes I used can be found on:

https://github.com/Vilbeee/Ville-s-Portfolio/blob/558cd0d50ebb0312ab83af03d793fb662e896897/S%26P500%20Project/Code/Power%20BI%20Dax%20Codes.txt

The entire Power BI dashboard as a .pbix file can be found on: 

https://github.com/Vilbeee/Ville-s-Portfolio/blob/558cd0d50ebb0312ab83af03d793fb662e896897/S%26P500%20Project/S%26P500%20Project.pbix

The entire Power BI dashboard as a .pdf file can be found on: 

https://github.com/Vilbeee/Ville-s-Portfolio/blob/558cd0d50ebb0312ab83af03d793fb662e896897/S%26P500%20Project/S%26P500%20Project.pdf

Example 1: Using DAX to create a card which showcases the company with the lowest non-positive P/E-Ratio

```DAX
Best P/E-Ratio = 
MINX(
    FILTER(
        'PE-Ratio', 
        'PE-Ratio'[pe_ratio] > 0
    ), 
    'PE-Ratio'[pe_ratio])
```

```DAX    
Company With The Best P/E-Ratio = 
VAR MinPE = [Best P/E-Ratio]
RETURN
    CALCULATE(
        FIRSTNONBLANK('Companies'[Company Name], 1),
        FILTER(
            'PE-Ratio',
            'PE-Ratio'[pe_ratio] = MinPE
        )
    )
```

Example 2: Calculating the highest dividend amount of the previous quarter and the highest current dividend yield.

```DAX
Highest Dividend From The Previous Quarter = 
CALCULATE(
    MAX('Dividends'[Dividend]),
    FILTER(
        'Dividends',
        RELATED('Date'[date]) >= DATE(2024, 7, 1) && 
        RELATED('Date'[date]) <= DATE(2024, 10, 1)
    )
)
```

```DAX
Highest Forward Dividend Yield = 
CALCULATE(
    MAX('Forward Dividend Yield'[forward_dividend_yield]),
    FILTER(
        'Forward Dividend Yield',
        RELATED('Date'[date]) >= DATE(2024, 9, 30) && 
        RELATED('Date'[date]) <= DATE(2024, 10, 1)
    )
)
```

Example 3: Calculating the Debt Ratio.

```DAX
Debt Ratio = 
VAR TotalDebt = 
    CALCULATE(
        SUM('Quarterly Balance Sheet'[total_debt]),
        'Quarterly Balance Sheet'[date] >= DATE(2024, 5, 31) &&
        'Quarterly Balance Sheet'[date] <= DATE(2024, 7, 31)
    )

VAR TotalAssets = 
    CALCULATE(
        SUM('Quarterly Balance Sheet'[total_assets]),
        'Quarterly Balance Sheet'[date] >= DATE(2024, 5, 31) &&
        'Quarterly Balance Sheet'[date] <= DATE(2024, 7, 31)
    )

RETURN 
    IF(TotalAssets <> 0, TotalDebt / TotalAssets, BLANK())
```

Example 4: I included a synced dropdown slicer for sectors to quickly and easily compare companies inside their own industries.

![Dropdown slicer](https://github.com/user-attachments/assets/da0a0682-a90a-4e71-b176-2b20b4ff9ec1)

Example 5: I included a tooltip with the company information whenever hovered on graphs. This way one doesn't have to remember each and every company's tickers. 

![Company information tooltip](https://github.com/user-attachments/assets/a9bf479a-1696-4e8f-b4c8-b085e7a5f123)

Example 6: I used conditional formatting for the column charts to get an idea of good and bad values at a glance.

![Conditionally formatted colours](https://github.com/user-attachments/assets/ec394c51-76d4-4f04-81d5-97665a4796fe)

Example 7: I used buttons to quickly hop between different financial ratios.

![Buttons](https://github.com/user-attachments/assets/f916f2f8-1e4d-4a48-a9f3-367f29792af7)

Example 8: I decided to create a night theme style dashboard as more and more people prefer dark themes and I personally do as well. These tones are easy for the eyes and the light colours on graphs pop out nicely.

### Project Questions

While the aim of the project was to create a dashboard which could be used for quick comparison between stocks and not necessarily answer any specific questions, I think it is good to demonstrate how well the final product works.

Question 1: Which technology company stock had the highest growth percentage in the past 5 years?

![Question 1](https://github.com/user-attachments/assets/7334de13-da1c-45fc-bc32-6e890240f861)

Answer: NVIDIA Corporation's stock price grew close to 2700% in 5 years, making them the clear winner.

Question 2: Who are the top 5 companies based on market cap?

![Question 2](https://github.com/user-attachments/assets/7031dd58-41b2-4f10-9095-6ad53deffd33)

Answer: Apple, Microsoft, Nvidia, Alphabet and Amazon.

Question 3: What is the median P/E-Ratio in the Consumer Cyclical sector?

First choose the sector on the dropdown slicer.

![Question 3 p1](https://github.com/user-attachments/assets/d3e00a4d-508b-4120-88d8-26a841a8a4b8)

Then see the results on the card visual.

![Question 3 p2](https://github.com/user-attachments/assets/f59a6ebf-1223-4314-a120-434e25221a60)

Answer: The median P/E-ratio for the Consumer Cyclical sector is 26,90. Which is a little bit lower than the overall median. The overall median is 27,21.

Question 4: Based on the profitability matrix, is there any standout companies that would be interesting from an investor's point of view?

![Question 4](https://github.com/user-attachments/assets/1cb482a1-e9e2-45b1-a2b5-8cf36ec24e2c)

Answer: According to the profitability matrix, the companies in the top right quadrant should interest an investor at a glance. The three standout companies at the top right are Johnson & Johnson, Abbvie Inc and Merck & Company Inc.

### Final thoughts

I believe I succeeded in my aim to create a dashboard, which can quickly answer questions about financial statements and ratios. My dashboard offers a good arsenal of useful financial ratios and other information, but it should not be used to make one's final decisions on which companies to invest in. Rather this dashboard should be a tool to quickly scan companies and sectors. This way one can weed out the bad stocks quickly and begin to further investigate the seemingly good ones.

While It would have been possible to add numerous other stock KPIs to the dashboard, I wanted to keep it straightforward and simple to use. My dashboard showcases some graphs for historical trend analysis, but the main focus is on KPIs calculated with the trailing twelve months (TTM) data such as price to earnings (P/E), debt to equity (D/E) and return on equity (ROE). This way one can get a quick look into companies' recent profitability and financial health before jumping into the finer details of the company performance.

Doing this project I was able to showcase how SQL, Power BI, Python and Excel can be extremely useful tools in one's everyday life. It can be a very helpful tool for people interested in investing as stock data is often quite readily available. I believe I was succesful in showing my personal skills when it comes to making use of these tools as well. 

#### Limitations and possible improvements

Using Yahoo Finance as the data source, had its limitations as some of the data was not available. This includes some of the most recent quarterly data as well as some of the older historical data. With more of the historical data, better trend analysis would be possible. 

Differences in availability of certain data makes it difficult to compare some companies. This also hinders the process of calculating different financial ratios. 

It is also important to acknowledge that companies in different sectors often behave in very different ways. This is why all of the financial ratios can not be used to compare companies in differing sectors. It is also good to understand that even if some ratios looked promising, it might not give you the full truth about the company. 
