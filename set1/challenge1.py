#!/bin/env python

import array
import base64
import sys

# python challenge1.py string_to_convert

print base64.encodestring(sys.argv[1].decode("hex"))

