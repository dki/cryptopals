#!/bin/env python

import aes
import sys
import base64

# python challenge7.py key < file.txt

print aes.decrypt(sys.argv[1], base64.decodestring(sys.stdin.read()))
