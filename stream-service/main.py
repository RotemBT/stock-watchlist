from typing import List
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.background import BackgroundTasks
from models import Stock, News
import websocket, json
import config
import ast

app = FastAPI()

socket = "wss://stream.data.alpaca.markets/v2/iex"
db: List[str] = ['AAPL', 'TSLA']

# demo db todo: change to redis 
db_stock_price = {}
db_news= {'AAPL':[]}

def on_open(ws):
    print("opened")
    auth_data = {"action": "auth", "key": config.API_KEY, "secret": config.SECRET_KEY}
    ws.send(json.dumps(auth_data))
    listen_message = {"action":"subscribe","trades":db, 'quotes':db ,'bars':db, "news": db}
    ws.send(json.dumps(listen_message))
    
def on_message(ws, message):
    print("received a message")
    message = ast.literal_eval(message)
    message = message[0]

    if message['T'] == 't':
        stock = Stock(
            symbol= message['S'],
            tradeId= int(message['i']),
            exchangeCode= message['i'],
            tradePrice= float(message['p']), 
            tradeSize= int(message['s']), 
            time= str(message['time']),
            )
        db_stock_price[message['S']] = stock

    elif message['T'] == 'n':
        n = News(
            id= int(message['id']), 
            headline= message['headline'], 
            summary= message['summary'], 
            author= message['author'], 
            timeCreated= message['created_at'], 
            timeUpdate=message['updated_at'], 
            url= message['url'], 
            content= message['content'], 
            symbol=message['symbols'][0],
            source= message['source']
            )
        db_news[News.symbol].append(n) 

    print(message)

def on_close(ws):
    print("closed connection")
    ws.close()

def websocket_connection(ws):
    BackgroundTasks.add_task(ws.run_forever(),'start ws')
    
ws = websocket.WebSocketApp(socket, on_open=on_open, on_message=on_message, on_close=on_close)

app.add_middleware(
    CORSMiddleware,
    allow_origins=['http://localhost:4000'],
    allow_methods=['*'],
    allow_headers=['*']
)

@app.get("/")
def root():
    return {"hello":"world"}

@app.get('/stocks')
async def stocks_to_watch():
    return {"list to watch": (',').join(db), "prices":db_stock_price}

@app.get('/watch')
def connect_to_websocket():
    websocket_connection(ws)
    return {'connection': 'successed'}

@app.get('/close')
def close_socket():
    on_close(ws)
    return {'close socket': 'successed'}

