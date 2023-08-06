import _global
import sys, time
from webSocket import wsSend

def postOrder(price):

    cid = int(round(time.time() * 1000))

    #amount = str(direction * _global.AMOUNT) + '.0'

    inputDetails = {
    'cid': cid,
    'type': 'EXCHANGE LIMIT',
    'symbol': _global.TICKER,
    'amount': _global.current_amount,
    'price': price,
    'flags': 4096
    }
    inputPayload = [0, 'on', None, inputDetails]
    wsSend(inputPayload)

def calculations():

    print ('Ask is:' + str(_global.bid_ask['ask']))
    print ('Bid is:' + str(_global.bid_ask['bid']))

    minimum_increment = round(1 / pow (10,_global.DECIMALS), _global.DECIMALS)

    # Place bid order

    bidAskDiff = round(_global.bid_ask['ask'] - _global.bid_ask['bid'], _global.DECIMALS)

    #print('Diff between bid and ask: ' + str(bidAskDiff))

    twiceTheIncrement = round(minimum_increment * 2, _global.DECIMALS)

    #print('Two times minimum increment: ' + str(twiceTheIncrement))

    if bidAskDiff > twiceTheIncrement: # i.e. Spread is enough to sell later: one increment for the bid one increment for the ask
        bidPrice = str(round(_global.bid_ask['bid'] + minimum_increment, _global.DECIMALS))
    
    else: # Move the order below so it is not executed
        bidPrice = str(round(_global.bid_ask['bid'] - (minimum_increment * 10), _global.DECIMALS))

    return bidPrice

def calculationsAsk():

    print ('Ask is:' + str(_global.bid_ask['ask']))
    print ('Bid is:' + str(_global.bid_ask['bid']))

    minimum_increment = round(1 / pow (10,_global.DECIMALS), _global.DECIMALS)

    # Place bid order

    bidAskDiff = round(_global.bid_ask['ask'] - _global.bid_ask['bid'], _global.DECIMALS)

    #print('Diff between bid and ask: ' + str(bidAskDiff))

    twiceTheIncrement = round(minimum_increment * 2, _global.DECIMALS)

    #print('Two times minimum increment: ' + str(twiceTheIncrement))

    if bidAskDiff >= twiceTheIncrement: # i.e. Spread is enough to sell later: one increment for the bid one increment for the ask
        askPrice = str(round(_global.bid_ask['ask'] - minimum_increment, _global.DECIMALS))
    
    else: # Move the order below so it is not executed
        askPrice = str(round(_global.bid_ask['ask'], _global.DECIMALS))

    return askPrice

def placeFirstOrders(data):
    #In the future take into account possible existing orders, for now assume no previous orders

    _global.current_amount = str(_global.AMOUNT) + '.0'

    bidPrice = calculations()

    print ('my first Bid will be: ' + bidPrice)
    postOrder(bidPrice)


def postModify(price):

    #amount = str(direction * _global.AMOUNT) + '.0'

    inputDetails = {
    'id': _global.order_id,
    'amount': _global.current_amount,
    'price': price
    }
    inputPayload = [0, 'ou', None, inputDetails]
    wsSend(inputPayload)

def modifyOrder(data):

    if _global.number_of_trades == 0:
        newPrice = calculations()
    else:
        newPrice = calculationsAsk()

    print ('the new price will be: ' + newPrice)
    postModify(newPrice)

# SELLING

def placeSellOrder(data):

    _global.current_amount = '-' + str(_global.AMOUNT) + '.0'

    askPrice = calculationsAsk()

    print ('myAsk will be: ' + askPrice)
    postOrder(askPrice)
