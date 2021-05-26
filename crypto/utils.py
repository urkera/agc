import hmac
import time
import base64
import hashlib


def get_headers(key, secret):
    secret = base64.b64decode(secret)
    stamp = str(int(time.time()) * 1000)
    data = "{}{}".format(key, stamp).encode("utf-8")
    signature = hmac.new(secret, data, hashlib.sha256).digest()
    signature = base64.b64encode(signature)
    headers = {"X-PCK": key, "X-Stamp": stamp,
               "X-Signature": signature, "Content-Type": "application/json"}
    return headers


def normalize_prices(data):
    result = {}
    keys = ['open', 'high', 'low', 'average', 'volume']
    for cur in data:
        temp = {'close': cur['last']}
        for key in keys:
            temp[key] = cur[key]
        result[cur['pairNormalized']] = temp
    return result
