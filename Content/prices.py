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


def getting_prices():
    prices = {}
    ticker_symbols = ["AAPL", "MSFT", "AMZN", "GOOGL", "TSLA", "META", "NVDA", "KO", "INTC", "V"]
    
    for ticker in ticker_symbols:
        stock = yf.Ticker(ticker)
        current_price = stock.history(period="1d")['Close'].iloc[-1]
        rounded_price = round(current_price, 2)
        company_name = stock.info['longName']  
        
        prices[company_name] = rounded_price
    
    return prices

print(getting_prices())

