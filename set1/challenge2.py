#!/bin/env python

import array
import util
import sys

# python challenge2.py string1 string2

c = array.array('B', sys.argv[1].decode('hex'))
k = array.array('B', sys.argv[2].decode('hex'))

print util.xor(k, c).tostring().encode('hex')
