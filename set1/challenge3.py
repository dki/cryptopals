import util
import array
import sys

# python challenge3.py xord_string

c = array.array('B', sys.argv[1].decode('hex'))
result = util.predict_single_xor(c)
print "key=%s; %s" % (hex(result["key"]), result["text"])
