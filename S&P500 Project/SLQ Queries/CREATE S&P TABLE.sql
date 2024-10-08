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
