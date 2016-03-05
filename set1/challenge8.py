import ecb
import sys

# python challenge8.py < file.txt

for line in sys.stdin.readlines():
    if ecb.is_ecb(line.rstrip().decode('hex')):
        print line
