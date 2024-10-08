SELECT ticker, date, 
current_assets/current_liabilities current_ratio, 
current_assets/(current_liabilities-inventory) quick_ratio 
FROM balance_sheet_quarter
WHERE date BETWEEN '2024-05-31' AND '2024-07-31';