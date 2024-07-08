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


#def getting_prices():
#    prices = {}
#    ticker_symbols = ["AAPL", "MSFT", "AMZN", "GOOGL", "TSLA", "META", "NVDA", "KO", "INTC", "V"]
#    
#    for ticker in ticker_symbols:
#        stock = yf.Ticker(ticker)
#        current_price = stock.history(period="1d")['Close'].iloc[-1]
#        rounded_price = round(current_price, 2)
#        company_name = stock.info['longName']  
#        
#        prices[company_name] = rounded_price
#    
#    return prices

class Price:
    def __init__(self):
        pass
    
    def get_price(self, ticker):
        stock = yf.Ticker(ticker)
        current_price = stock.history(period="1d")['Close'].iloc[-1]
        return round(current_price, 2)
    
    def google_price(self):
        return self.get_price("GOOGL")
    
    def apple_price(self):
        return self.get_price("AAPL")
    
    def microsoft_price(self):
        return self.get_price("MSFT")
    
    def amazon_price(self):
        return self.get_price("AMZN")
    
    def tesla_price(self):
        return self.get_price("TSLA")
            
    def Nvidia_price(self):
        return self.get_price("NVDA")

    def Visa_price(self):
        return self.get_price("TSLA")

    def Coca-Cola_price(self):
        return self.get_price("KO")

    def Intel_price(self):
        return self.get_price("INTC")
        
    def Meta_price(self):
        return self.get_price("META")