import os

def hexToBytes(x):
    return [int(x[i:i+2], 16) for i in range(0, len(x), 2)]

def bytesToHex(x):
    return "".join(["%02x" % x[i] for i in range(len(x))])

def bytesToStr(x):
    return "".join(map(chr, x))

def strToBytes(x):
    return map(ord, x)

class SeedStorage(object):
    def __init__(self, name, pw):
        self.filename = os.path.expanduser('~/.totp/' + name)
        self.pw = map(ord, pw)

    def xor(self, seed):
        pwlen = len(self.pw)
        return [seed[i] ^ self.pw[i % pwlen] for i in range(len(seed))]

    def get(self):
        f = open(self.filename)
        raw = f.readline()
        f.close()

        seed = hexToBytes(raw)
        return bytesToStr(self.xor(seed))

    def save(self, seed):
        seed = strToBytes(seed)

        f = open(self.filename, 'w')
        f.write(bytesToHex(self.xor(seed)))
        f.close()
