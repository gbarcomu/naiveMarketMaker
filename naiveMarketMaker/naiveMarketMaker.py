import websocket
import _global
from datetime import datetime
import os, json, hmac, hashlib
from handleEvents import handleEvent
from handleData import handleData
from buildAuthMessage import build_autentication_message
import requests
from webSocket import connect_ws

#CONFIG

WS_PUB_ENDPOINT = 'wss://api-pub.bitfinex.com/ws/2'
WS_AUTH_ENDPOINT = 'wss://api.bitfinex.com/ws/2'
REST_PUB_ENDPOINT = 'https://api-pub.bitfinex.com/v2'

API_KEY, API_SECRET = (
    os.getenv("BFX_API_KEY"),
    os.getenv("BFX_API_SECRET")
)

#HANDLERS

def on_message(ws, message):
    data = json.loads(message)
    # Handle events
    if 'event' in data:
        handleEvent(data)
    else:
        handleData(data)      

def on_error(ws, error):
    print(error)

def on_close(ws):
    print('### API connection closed ###')
    os._exit(0)

def on_open(ws):
    print('API connected')
    ticker = {
        'event': 'subscribe',
        'channel': 'ticker',
        'symbol': _global.TICKER
    }
    ws.send(json.dumps(ticker))

    ws.send(json.dumps(build_autentication_message(API_KEY, API_SECRET)))

def getFirstBidAsk():
    response = requests.get(f"{REST_PUB_ENDPOINT}/ticker/{_global.TICKER}")
    ticker_raw = json.loads(response.text)
    _global.bid_ask = {
        'bid': ticker_raw[0],
        'ask': ticker_raw[2],
    }
    print('First bid: ' + str(_global.bid_ask['bid']) + '\n' + 'First ask: ' + str(_global.bid_ask['ask']))

getFirstBidAsk()
connect_ws(WS_AUTH_ENDPOINT, on_message, on_error, on_close, on_open)