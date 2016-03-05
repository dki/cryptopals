#!/bin/env python

import array
import base64
import sys
from collections import Counter

# key and text are assumed to be byte arrays
def xor(key, text):
    result = array.array('B')
    keylen = len(key)

    for i in range(0, len(text)):
        result.append(key[i%keylen] ^ text[i])

    return result 

# a1 and a2 are assumed to be byte arrays
def compute_hamming(a1, a2):
    score = 0
    for i in range(0, len(a1)):
        byte1 = '{0:08b}'.format(a1[i])
        byte2 = '{0:08b}'.format(a2[i])
        for j in range(0, len(byte1)):
            if byte1[j] != byte2[j]:
                score += 1
    return score

# letter frequency scores
letters = { ' ':13, 
            'E':12.7, 
            'T':9.0, 
            'A':8.16, 
            'O':7.5, 
            'I':6.96, 
            'N':6.74, 
            'S':6.32, 
            'R':5.98, 
            'H':6.09, 
            'D':4.25, 
            'L':4.02, 
            'U':2.75, 
            'C':2.78, 
            'M':2.40, 
            'F':2.22, 
            'Y':1.97, 
            'W':2.36, 
            'G':2.01, 
            'P':1.92, 
            'B':1.49, 
            'V':0.97, 
            'K':0.77
          }

# a is assumed to be a byte array
def predict_single_xor(a):
    cipher_scores = {}
    cipher_plaintexts = {}
    for cipher in range(0, 255):
        c = array.array('B')
        score = 0
        for i in range(0, len(a)):
            c.append(a[i] ^ cipher)
        else:
            s = Counter(c.tostring())
            common = s.most_common()
            for letter, count in common:
                if letter.upper() in letters:
                    score += count * letters[letter.upper()]
            if score > 0:
                cipher_scores[cipher] = score
                cipher_plaintexts[cipher] = c.tostring()

    if len(cipher_scores) > 0:
        winner = max(cipher_scores, key=cipher_scores.get)
        return {    'key': winner,  
                    'score': max(cipher_scores.values()), 
                    'text': cipher_plaintexts[winner] 
               }

    return None

# to initialize default_dict
def default_array():
    return array.array('B')

# inputs are assumed to be byte arrays
def normalized_hamming(ciphertext, keysize):
    score = 0
    num_blocks = (len(ciphertext) / keysize) - 1

    for i in range(0, num_blocks):
        score += compute_hamming(ciphertext[i*keysize:(i+1)*keysize], ciphertext[(i+1)*keysize:(i+2)*keysize])

    return float(score) / keysize / num_blocks

