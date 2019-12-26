import hmac
import base64
import struct
import hashlib
import time

class TOTP(object):
    def __init__(self, secret, digits=6):
        self.secret = base64.b32decode(secret, True)
        self.digits = digits

    def gen(self):
        h = hmac.new(self.secret, self.getMsg(), hashlib.sha1).digest()
        offset = ord(h[-1]) & 0xf
        result = (struct.unpack(">I", h[offset:offset+4])[0] & 0x7fffffff)
        return self.padLeft(str(result % 10 ** self.digits))

    def getMsg(self):
        return struct.pack(">Q", int(time.time())//30)

    def padLeft(self, h):
        return '0'*(self.digits - len(h)) + h


