#!/bin/env python

import array
import sys
import util
import base64
import operator
from collections import defaultdict

# python challenge6.py file.txt

scores = {}
with open(sys.argv[1], 'rb') as f:
    ciphertext = array.array('B', base64.decodestring(f.read()))
for keysize in range(2, 41):
    scores[keysize] = util.normalized_hamming(ciphertext, keysize)

chosen_keysize = min(scores, key=scores.get)
print "Min Hamming score: %s for keysize: %i" % (scores[chosen_keysize], chosen_keysize)
#for (ks, hs) in sorted(scores.items(), key=operator.itemgetter(1)):
#    print "%02i: %f" % (ks, hs)


#chosen_keysize = int(raw_input("Which keysize? "))
blocks = defaultdict(util.default_array)

for i in range(0, len(ciphertext)):
    blocks[i % chosen_keysize].append(ciphertext[i])

key = array.array('B')
for k in blocks:
    key.append(util.predict_single_xor(blocks[k])['key'])

print "Predicted key: %s" % key.tostring()

#chosen_key = array.array('B', raw_input("Enter key [leave blank to use found key]: "))

#if len(chosen_key) == 0:
#    chosen_key = key

print "Decrypted text:\n"
print util.xor(key, ciphertext).tostring()
        
