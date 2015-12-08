import base64
import binascii
import codecs

#def hex_to_base64(data, byte_array):
#    return base64.b64encode(byte_array.fromhex(data)).decode()

def bytes_to_base64(data):
    return base64.b64encode(data).decode()

def base64_to_bytes(data):
    return base64.b64decode(data)

def bytes_to_hex(data):
    return binascii.b2a_hex(data).decode()

def hex_to_base64(data):
    return bytes_to_base64(hex_to_bytes(data))

def hex_to_bytes(data):
    bytes = bytearray(data, encoding='utf-8')
    return bytes.fromhex(data)

def string_to_bytes(data):
    return data.encode('utf-8')


# Matasano crypto challenges

def challenge_1():
    """
    http://cryptopals.com/sets/1/challenges/1/
    Convert hex to base64

    The string:
    49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d

    Should produce:
    SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t
    """
    goal = u'SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t'
    data = u'49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d'
    #print data

    #h = hex_to_bytes(data)
    #print h

    #b64 = bytes_to_base64(h)
    #print b64

    result = hex_to_base64(data)
    #print result

    assert result == goal, "Challenge #1 failed"


def challenge_2():
    """
http://cryptopals.com/sets/1/challenges/2/

Fixed XOR

Write a function that takes two equal-length buffers and produces their XOR combination.
If your function works properly, then when you feed it the string:

    1c0111001f010100061a024b53535009181c

... after hex decoding, and when XOR'd against:

    686974207468652062756c6c277320657965

... should produce:

    746865206b696420646f6e277420706c6179

    
    """
    goal = '746865206b696420646f6e277420706c6179'

    b1 = '1c0111001f010100061a024b53535009181c'
    b2 = '686974207468652062756c6c277320657965'
    bh1 = int(b1, 16)
    bh2 = int(b2, 16)
    result = hex(bh1^bh2)
    result = result.lstrip('0x').rstrip('L')
    #print result
    #print result.decode("hex")

    assert result == goal, "Challenge #2 failed"
    

def challenge_3():
    """
http://cryptopals.com/sets/1/challenges/3/
Single-byte XOR cipher

The hex encoded string:

1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736

... has been XOR'd against a single character. Find the key, decrypt the message.

You can do this by hand. But don't: write code to do it for you.

How? Devise some method for "scoring" a piece of English plaintext. Character frequency is a good metric. Evaluate each output and choose the one with the best score.     
    """
    enc = u'1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736'
    

if __name__ == '__main__':
    challenge_1()
    challenge_2()
    challenge_3()

