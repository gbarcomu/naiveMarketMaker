import _global
import json
from orderExecution import placeFirstOrders, modifyOrder, placeSellOrder

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
                modifyOrder(data)

        if 'zero' in _global.channels[channel_id]:
            if data[1] == 'hb':
                # Ignore heartbeat messages
                pass
            elif data[1] == 'os':
                if _global.START_SELLING == False:
                    placeFirstOrders(data)
                else:
                    _global.number_of_trades = 1
                    placeSellOrder(data)
            elif data[1] == 'on':
                print_myOrders(data)
                _global.order_id = data[2][0]
                print ('Order new: ' + str(_global.order_id))
            # elif data[1] == 'oc':
            #     print_myOrders(data)
            # elif data[1] == 'ou':
            #     print ('Order modified')
            #     print_myOrders(data)

            # elif data[1] == 'bu':
            #     print ('Balance')
            #     print_myOrders(data)

            elif data[1] == 'te':
                if _global.number_of_trades == 0:
                    print ('First trade has been executed')
                    _global.number_of_trades = 1
                    placeSellOrder(data)
                else:
                    print ('Second trade has been executed')
                    exit()