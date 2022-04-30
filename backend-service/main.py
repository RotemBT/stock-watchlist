from fastapi import FastAPI, HTTPException, WebSocket
from fastapi.middleware.cors import CORSMiddleware
from typing import List
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=['http://localhost:8000'],
    allow_methods=['*'],
    allow_headers=['*']
)
db: List[str] = []

@app.get("/")
def root():
    return {"hello":"world"}

@app.get('/stocks')
async def get_stocks_list():
    return {'folowing stocks': db}

@app.get('/stocks/{stock}')
async def get_stock_data(symbol: str):
    for stock in db:
        if stock == symbol:
            return { "stock": stock }
    raise HTTPException(status_code= 404, detail= f"stock {symbol} not in watch list")

@app.post('/stocks/{stock}')
async def watch(new_stock: str):
    for stock in db:
        if stock == new_stock:
            raise HTTPException(status_code=409, detail=f'stock {new_stock} already exist')
    db.append(new_stock)
    return { f'{new_stock}' : 'added succesfully'}


@app.delete('/stocks/{stock}')
async def unwatch(symbol: str):
    for stock in db:
        if stock == symbol:
            db.remove(symbol)
            return {f"stock {symbol}": "removed successfully"}
    raise HTTPException(status_code= 404, detail= f"stock {symbol} not in watch list")      
