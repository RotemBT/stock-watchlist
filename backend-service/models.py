import string
from pydantic import BaseModel
from typing import List

class Stock(BaseModel):
    message: str
    symbol: str
    tradeId: int
    exchangeCode: str
    tradePrice: float
    tradeSize: int
    time: string
    tradeCondition: List[str]
    tape: str


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


class News(BaseModel):
    message: str
    timeCreated: str
    timeUpdate: str
    author: str
    summary:str
    content: str
    url: str
    symbol: List[str]
    source: str
    id: int