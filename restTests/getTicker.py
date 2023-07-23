import struct
from datetime import datetime
import os, json, hmac, hashlib
import requests

API = "https://api-pub.bitfinex.com/v2"

# API_KEY, API_SECRET = (
#     os.getenv("BFX_API_KEY"),
#     os.getenv("BFX_API_SECRET")
# )

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

endpoint = "/ticker/tXAUTF0:USTF0"

payload = {
    # "type": "EXCHANGE LIMIT",
    # "symbol": "tBTCUSD",
    # "amount": "0.165212",
    # "price": "30264.0"
}

headers = {
    # "Content-Type": "application/json",
    # **_build_authentication_headers(endpoint, payload)
}

response = requests.get(f"{API}/{endpoint}")

responseArray = json.loads(response.text)

print('Ask price: ', responseArray[0])
print('Bid prie: ', responseArray[2])