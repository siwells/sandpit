#!/usr/bin/env

def batteries_included(s):
    from codecs import encode
    return encode(source, 'rot13')

def rot13(s):
    def lookup(v):
        o, c = ord(v), v.lower()
        if 'a' <= c <= 'm':
            return chr(o+13)
        if 'n' <= c <= 'z':
            return chr(o-13)
        return v
    return ''.join(map(lookup, s))

def alphabet_shift(n):
    from string import ascii_lowercase as lc, ascii_uppercase as uc
    import string as st
    lookup = st.maketrans(lc + uc, lc[n:] + lc[:n] + uc[n:] + uc[:n])
    return lambda s: s.translate(lookup)

if __name__ == "__main__":
    source = 'HELLO WORLD'
    print batteries_included(source)
    print rot13(source)
    print alphabet_shift(13)(source)

