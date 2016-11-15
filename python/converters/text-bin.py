#!/usr/bin/env

if __name__ == "__main__":
    source = 'HELLO WORLD'
    print ' '.join(format(ord(x), 'b') for x in source)
    print ' '.join(format(x, 'b') for x in bytearray(source))
    print ' '.join(map(bin,bytearray(source)))
    print ' '.join(map(bin,bytearray(source, 'utf8')))
