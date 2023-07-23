print("Get my orders")

from datetime import datetime
import os, json, hmac, hashlib
import requests

API = "https://api.bitfinex.com/v2"

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

endpoint = "auth/r/orders"

payload = {
    # "type": "EXCHANGE LIMIT",
    # "symbol": "tBTCUSD",
    # "amount": "0.165212",
    # "price": "30264.0"
}

headers = {
    "Content-Type": "application/json",
    **_build_authentication_headers(endpoint, payload)
}

response = requests.post(f"{API}/{endpoint}", json=payload, headers=headers)

print(response.content)