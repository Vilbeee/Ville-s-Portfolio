SELECT ticker, total_debt, stockholders_equity, total_debt/stockholders_equity de_ratio
FROM balance_sheet_quarter
WHERE date BETWEEN '2024-05-31' AND '2024-07-31';