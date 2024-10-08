SELECT bsq.ticker, AVG(stockholders_equity) average_stockholders_equity, MAX(net_income)/AVG(stockholders_equity)*100 ROE
FROM balance_sheet_quarter bsq
JOIN income_statement_ttm ist
ON bsq.ticker = ist.ticker
GROUP BY bsq.ticker
ORDER BY ROE DESC;