# Discord-Bitmex-Bot
Retrieve Bitmex data from Discord

This code uses Bitmex API endpoints to retrieve market data from Discord.

- Functions

- get_announcements()
	- get latest announcements from Bitmex
	- data returned as dictionary type

- markets()
	- return available markets from Bitmex
	- data returned as a list data type

- last_trade(ticker)
	- return last trade data from specific ticker
	- receive one string argument(ticker)
	- if ticker is not valid return string with available tickers
	- if ticker is valid return string with market data

