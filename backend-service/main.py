from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from alpaca_trade_api.rest import REST, TimeFrame
import config
from typing import List

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*']
)
stockWatch: List[str] = []

@app.get("/")
def root():
    return {'hello':'world'}

@app.post('/api/news')
async def get_stocks_list(stocks: str):
    global stockWatch
    stocksList = stocks.split(',')
    stockWatch.extend(stocksList)
    stockWatch = list(set(stockWatch))
    rest_client = REST(config.API_KEY, config.SECRET_KEY)
    news = rest_client.get_news(stocks, config.NEWS_START_DATE, config.NEWS_END_DATE)
    newsFormatted = []
    for n in news:
        newsFormatted.append(n._raw)
    return newsFormatted
    
@app.post('/api/bars')
async def get_stocks_list(bars: str):
    global stockWatch
    stocksList = bars.split(',')
    stockWatch.extend(stocksList)
    stockWatch = list(set(stockWatch))
    rest_client = REST(config.API_KEY, config.SECRET_KEY)
    bars = rest_client.get_bars_iter(bars, TimeFrame.Day, config.BARS_START_DATE, config.BARS_END_DATE, adjustment='raw')
    barsFormatted = []
    for n in bars:
        barsFormatted.append(n._raw)
    return barsFormatted
