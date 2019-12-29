import hmac
from struct import pack, unpack
import hashlib
from time import time

digits = 6

def getInterval():
    return pack(">Q", int(time())//30)

def padLeft(h):
    return '0'*(digits - len(h)) + h

def getCode(secret):
    h = hmac.new(secret, getInterval(), hashlib.sha1).digest()
    offset = ord(h[-1]) & 0xf
    result = unpack(">I", h[offset:offset+4])[0] & 0x7fffffff
    return padLeft(str(result % 10 ** digits))




