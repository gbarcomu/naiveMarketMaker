print("Create Order")

from datetime import datetime
import os, json, hmac, hashlib
import requests

API_AUTH = "https://api.bitfinex.com/v2"
API_PUBLIC = "https://api-pub.bitfinex.com/v2"

API_KEY, API_SECRET = (
    os.getenv("BFX_API_KEY"),
    os.getenv("BFX_API_SECRET")
)

def _build_authentication_headers(endpoint, payload = None):
    nonce = str(round(datetime.now().timestamp() * 1_000))

    message = f"/api/v2/{endpoint}{nonce}"

    if payload != None:
        message += json.dumps(payload)

    signature = hmac.new(
        key=API_SECRET.encode("utf8"),
        msg=message.encode("utf8"),
        digestmod=hashlib.sha384
    ).hexdigest()

    return {
        "bfx-apikey": API_KEY,
        "bfx-nonce": nonce,
        "bfx-signature": signature
    }

endpointTicker = "/ticker/tXAUTF0:USTF0"
endpointCreate = "auth/w/order/submit"
endpointView = "auth/r/orders"

payload = {
    "type": "LIMIT",
    "symbol": "tXAUTF0:USTF0",
    "amount": "0.01",
    "price": None
}

responseTicker = requests.get(f"{API_PUBLIC}/{endpointTicker}")

responseTickerParsed = json.loads(responseTicker.text)

print('Bid price: ', responseTickerParsed[0])
print('Ask prie: ', responseTickerParsed[2])

newBidPrice = float(responseTickerParsed[2]) - 0.1

print(newBidPrice)

payload['price'] = str(newBidPrice)

headers = {
    "Content-Type": "application/json",
    **_build_authentication_headers(endpointCreate, payload)
}

print(payload)

responseCreate = requests.post(f"{API_AUTH}/{endpointCreate}", json=payload, headers=headers)

print(responseCreate.text)