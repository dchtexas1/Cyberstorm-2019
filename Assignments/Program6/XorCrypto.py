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
from binascii import hexlify, unhexlify
#variables that can be changed
key2use = "key"

def encode(message, key):
    return hexlify(''.join(chr(ord(a)^ord(b)) for a, b in zip(message,key)))

def decode(message, key):
    return unhexlify(''.join(chr(ord(a)^ord(b)) for a, b in zip(message,key)))



encoded = encode(sys.argv[1], sys.argv[2])
print encode(sys.argv[1], sys.argv[2])
