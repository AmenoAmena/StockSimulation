import yfinance as yf
import asyncio

def fetch_price(ticker):
    stock = yf.Ticker(ticker)
    current_price = stock.history(period="1d")['Close'].iloc[-1]
    return round(current_price, 2)

async def get_price(ticker):
    return await asyncio.to_thread(fetch_price, ticker)


