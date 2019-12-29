from getpass import getpass
from seedstorage import SeedStorage
from code import getCode

def usage():
    print("totp <command> <name>")
    print("commands:")
    print("  add <name>: add new seed")
    print("  get <name>: print the code")

def main(argv):
    if len(argv) < 3:
        usage()
        exit()

    [ _, cmd, name ] = argv[:3]

    if cmd not in ['add', 'get']:
        usage()
        exit()
    
    storage = SeedStorage(name, getpass())

    if cmd == 'get':
        seed = storage.get()
        code = getCode(seed) 
        print(code)

    if cmd == 'add':
        seed = getpass('Seed:')
        storage.save(seed)

