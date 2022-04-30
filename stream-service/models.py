import string
from pydantic import BaseModel
from typing import List


class News(BaseModel):
    headline: str
    timeCreated: str
    timeUpdate: str
    author: str
    summary:str
    content: str
    url: str
    symbol: List[str]
    source: str
    id: int

class Stock(BaseModel):
    symbol: str 
    tradeId: int
    exchangeCode: str
    tradePrice: float
    tradeSize: int
    time: str

class Quote(BaseModel):
    message: str
    symbol: str
    askExchangeCode: str
    askPrice: float
    asdkSize: int
    bidExchangeCode: str
    bidPrice: float
    bidSize: int
    tradeSize: int
    time: str
    quoteCondition: List[str]
    tape: str

class MinuteBar(BaseModel):
    message: str
    symbol: str
    openPrice: float
    closePrice: float
    lowPrice: float
    highPrice: float
    volume: int
    time: str
