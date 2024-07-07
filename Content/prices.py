import yfinance as yf

ticker_symbol = "AAPL"
stock = yf.Ticker(ticker_symbol)
current_price = stock.history(period="1d")['Close'][-1]
rounded_price = round(current_price)
print(f"The current price of {ticker_symbol} is: ${rounded_price}")
