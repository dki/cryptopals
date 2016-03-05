#!/bin/env python

import util
import sys
import array

# python challenge4.py file.txt

scores = {}
with open(sys.argv[1], 'rb') as f:
    for line in f:
        result = util.predict_single_xor(array.array('B', line.rstrip().decode('hex')))
        if result is not None:
            scores["%s:%s" % (line.rstrip(), result["text"])] = result["score"]

if len(scores) > 0:
    print max(scores, key=scores.get)
        
