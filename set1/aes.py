from Crypto.Cipher import AES
import sys
import base64

def decrypt(key, ciphertext, iv=None,  mode=AES.MODE_ECB):
    decryptor = AES.new(key, mode)
    return decryptor.decrypt(ciphertext)


if __name__ == "__main__":
#    print decrypt(sys.argv[1], base64.decodestring(sys.stdin.read()))
    print decrypt(sys.argv[1], sys.stdin.read().rstrip().decode('hex'))
