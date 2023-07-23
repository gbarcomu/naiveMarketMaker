import _global
import json
from orderExecution import placeFirstOrders

def print_tickers(data):
    ticker_raw = data[1]
    _global.bid_ask = {
        'bid': ticker_raw[0],
        'ask': ticker_raw[2],
    }
    print('Bid: ' + str(_global.bid_ask['bid']) + '\n' + 'Ask: ' + str(_global.bid_ask['ask']))

def print_myOrders(data):
    print(data)
    
def handleData(data):
    channel_id = data[0]
    if channel_id in _global.channels:
        if 'ticker' in _global.channels[channel_id]:
            if data[1] == 'hb':
                # Ignore heartbeat messages
                pass
            else:
                print_tickers(data)

        if 'zero' in _global.channels[channel_id]:
            if data[1] == 'hb':
                # Ignore heartbeat messages
                pass
            elif data[1] == 'os':
                placeFirstOrders(data)
            elif data[1] == 'on' or data[1] == 'oc':
                print_myOrders(data)