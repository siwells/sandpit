#!/usr/bin/env

import binascii

if __name__ == "__main__":
    source = 'hello world'
    print ' '.join(map(str, [ord(c) for c in source]))
