from os import path, mkdir
from base64 import b32decode
import struct
import hashlib

root = path.expanduser('~/.totp/')

def xor(a, b):
    return bytearray(a[i] ^ b[i] for i in range(len(a)))

def hashPassword(pw):
    return bytearray(hashlib.sha1(pw).digest())[:10]

class SeedStorage(object):
    def __init__(self, name, pw):
        if not path.isdir(root):
            mkdir(root)
        self.filename = path.join(root, name)
        self.pw = hashPassword(pw)

    def get(self):
        f = open(self.filename, 'rb')
        seed = bytearray(f.read())
        f.close()

        return xor(seed, self.pw)

    def save(self, seed):
        seed = bytearray(b32decode(seed, True))

        f = open(self.filename, 'wb')
        f.write(xor(seed, self.pw))
        f.close()
