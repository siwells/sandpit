#!/usr/bin/env

import base64

if __name__ == "__main__":
    source = 'HELLO WORLD'
    print base64.b64encode(bytes(source))
    print base64.b64encode(source.encode('ascii'))
    print base64.b64encode(source.encode('utf-8'))
