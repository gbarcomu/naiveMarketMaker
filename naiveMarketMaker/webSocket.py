import websocket
from datetime import datetime
import os, json, hmac, hashlib, time
import _global

def connect_ws(ws_auth_endpoint, on_message, on_error, on_close, on_open):
    global ws
    websocket.enableTrace(False)
    ws = websocket.WebSocketApp(ws_auth_endpoint,
                            on_message = on_message,
                            on_error = on_error,
                            on_close = on_close,
                            on_open = on_open)
    ws.run_forever()

def wsSend(inputPayload):
    ws.send(json.dumps(inputPayload))


