import yfinance as yf


#Apple Inc. (AAPL)
#Microsoft Corporation (MSFT)
#Amazon.com Inc. (AMZN)
#Alphabet Inc. (GOOGL)
#Tesla, Inc. (TSLA)
#Meta Platforms, Inc. (META)
#NVIDIA Corporation (NVDA)
#Coca-Cola Company (KO)
#Intel Corporation (INTC)
#Visa Inc. (V)


def get_price(ticker):
    stock = yf.Ticker(ticker)
    current_price = stock.history(period="1d")['Close'].iloc[-1]
    return round(current_price, 2)
