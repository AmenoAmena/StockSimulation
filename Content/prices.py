import yfinance as yf

def get_price(ticker):
    stock = yf.Ticker(ticker)
    current_price = stock.history(period="1d")['Close'].iloc[-1]
    return round(current_price, 2)
