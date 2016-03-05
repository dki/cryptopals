import sys
import base64

def is_ecb(c):
    while len(c) > 16:
        if c[0:15] in c[16:]:
            return True
        else:
            c = c[16:]

    return False


if __name__ == "__main__":
    for line in sys.stdin.readlines():
        if is_ecb(line.rstrip().decode('hex')):
            print "Found dupe:"
            print line
        
