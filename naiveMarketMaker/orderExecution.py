import _global
import sys, time
from webSocket import wsSend

def postOrder(price):

    cid = int(round(time.time() * 1000))

    inputDetails = {
    'cid': cid,
    'type': 'LIMIT',
    'symbol': _global.TICKER,
    'amount': '1.0',
    'price': price
    }
    inputPayload = [0, 'on', None, inputDetails]
    wsSend(inputPayload)

def placeFirstOrders(data):
    print(data)
    #In the future take into account possible existing orders, for now assume no previous orders

    print ('Ask is:' + str(_global.bid_ask['ask']))
    print ('Bid is:' + str(_global.bid_ask['bid']))
    print(_global.DECIMALS)
    minimum_increment = 1 / pow (10,_global.DECIMALS)
    print(minimum_increment)

    # Place bid order

    bidPrice = str(round(_global.bid_ask['ask'] - (minimum_increment * 100), _global.DECIMALS))

    print ('myBid will be: ' + bidPrice)
    #postOrder(bidPrice)

    # Place ask order

    askPrice = str(-round(_global.bid_ask['bid'] + (minimum_increment * 100), _global.DECIMALS))

    print ('myAsk will be: ' + askPrice)
    #postOrder(askPrice)