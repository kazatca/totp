#!/usr/bin/python
from getpass import getpass
import pyperclip
from seedstorage import SeedStorage
from totp import TOTP

def main(argv):
    if len(argv) < 3:
        print "totp <command> <name> [seed]"
        print "commands:"
        print "  add: add new seed"
        print "  get: get code"
        print "  cp: copy code to clipboard"
        exit()

    [ app, command, name ] = argv[:3]

    storage = SeedStorage(name, getpass())

    if command == 'cp' or command == 'get':
        otp = TOTP(storage.get())
        code = otp.gen()

        if command == 'cp':
            pyperclip.copy(code)

        if command == 'get':
            print code

    if command == 'add':
        storage.save(args[1])

