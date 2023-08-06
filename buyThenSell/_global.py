#CONFIG
TICKER = 'tADAUST'
DECIMALS = 5
AMOUNT = 5
FLAGS = 4096 #POST ONLY

TRACE = True
START_SELLING = False

#STATE
channels = {0: 'zero'}
bid_ask = {}
order_id = None
number_of_trades = 0
current_amount = None