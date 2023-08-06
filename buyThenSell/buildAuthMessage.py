from datetime import datetime
import os, json, hmac, hashlib

def build_autentication_message(api_key, api_secret):
    message = { "event": "auth" }
    
    message["apiKey"] = api_key

    message["authNonce"] = round(datetime.now().timestamp() * 1_000)

    message["authPayload"] = f"AUTH{message['authNonce']}"

    message["authSig"] = hmac.new(
        key=api_secret.encode("utf8"),
        msg=message["authPayload"].encode("utf8"),
        digestmod=hashlib.sha384
    ).hexdigest()

    return message