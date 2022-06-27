from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import config
import alpaca_trade_api
from typing import List
import redis
alpacaAPI = alpaca_trade_api.rest
app = FastAPI()
redis = redis.Redis(host='localhost', port=6379, db=0)

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
    return {'hello': 'world'}


@app.get('/api/news')
async def get_stocks_list(stocks: str):
    global stockWatch
    stocksList = stocks.split(',')
    stockWatch.extend(stocksList)
    stockWatch = list(set(stockWatch))
    rest_client = alpacaAPI.REST(config.API_KEY, config.SECRET_KEY)
    news = rest_client.get_news(
        stocks, config.NEWS_START_DATE, config.NEWS_END_DATE)
    newsFormatted = []
    for n in news:
        newsFormatted.append(n._raw)
    return {'news': newsFormatted}


@app.get('/api/bars')
async def get_stocks_list(stock: str):
    cachedBars = redis.get(stock)
    if cachedBars:
        return {stock: cachedBars}
    rest_client = alpacaAPI.REST(config.API_KEY, config.SECRET_KEY)
    data = rest_client.get_bars_iter(
        stock, alpacaAPI.TimeFrame.Day, config.BARS_START_DATE, config.BARS_END_DATE, adjustment='raw')
    barsFormatted = []
    for n in data:
        barsFormatted.append(n._raw)
    redis.set(stock, barsFormatted)
    return {stock: barsFormatted}
