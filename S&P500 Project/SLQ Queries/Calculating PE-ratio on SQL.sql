SELECT sp.date, 
ist.ticker, 
sp.adjusted_close/ist.diluted_eps pe_ratio
FROM income_statement_ttm ist
JOIN s_and_p_daily sp
ON ist.ticker = sp.symbol
WHERE sp.date = '2024-09-30';