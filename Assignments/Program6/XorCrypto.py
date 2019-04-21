##############################################################################
# GitHub Repo Link: https://github.com/dchtexas1/Cyberstorm-2019
# https://github.com/dchtexas1/Cyberstorm-2019/tree/master/Assignments/Program3
#
# CSC 442
# Date: 04/02/19
# Team Name: Romans
# Names: Brady Anderson, Sam Dominguez, Dax Henson, Michael McCrary,
#        Daniel Munger, Stephanie Niemiec, Holland Wolf
#
# Description: Decodes message using an XOR Crypto method.
#
# Run Instructions: python chat_client.py
#
##############################################################################\

import sys
from binascii import hexlify

#sets our key to open a file in the current directory
file_object = open("key",'r')

class XORCrypto(object):

    def __init__(self, message, key):
        self.message = message
        self.key = key

    def XOR(self, message, key):
            return self.encode(message, key)

    def encode(self, message, key):
        return hexlify(''.join(chr(ord(a)^ord(b)) for (a, b) in zip(message,key)))




xor = XORCrypto(sys.argv[1],file_object)
xor.XOR(sys.argv[1],file_object)


#TODO: Need to find a way to read "a" and "b" bit by bit if possible, maybe in chunks. Then use
#Brady's Binary Decoder Class to decode probably
