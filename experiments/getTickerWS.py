import websocket
import json

def on_message(ws, message):
    print(message)

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
        'symbol': 'tBTCUSD'
    }
    ws.send(json.dumps(ticker))


def connect_api():
    global ws
    websocket.enableTrace(False)
    ws = websocket.WebSocketApp('wss://api-pub.bitfinex.com/ws/2',
                            on_message = on_message,
                            on_error = on_error,
                            on_close = on_close,
                            on_open = on_open)
    ws.run_forever()

connect_api()
simplePrint()