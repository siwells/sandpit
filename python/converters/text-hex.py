#!/usr/bin/env

import binascii

if __name__ == "__main__":
    source = 'hello world'
    #print bin(int(binascii.hexlify(source),16))
    print source.encode("hex")
    
    toHex = lambda x:" ".join([hex(ord(c))[2:].zfill(2) for c in x])
    print toHex(source)

