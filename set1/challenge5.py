#!/bin/env python

import util
import array
import sys

# python challenge5.py key plaintext.txt

key = array.array('B', sys.argv[1])
with open(sys.argv[2], 'rb') as f:
    plaintext = array.array('B', f.read().rstrip())

ciphertext = array.array('B')
keylen = len(key)

print util.xor(key, plaintext).tostring().encode("hex")

