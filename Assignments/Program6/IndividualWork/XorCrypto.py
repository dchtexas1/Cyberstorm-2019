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
# Run Instructions (key): XorCrypto.py < ciphertext
# Run Instructions (key2): XorCrypto.py < ciphertext2 > new_file
#
##############################################################################\

# Imports command line arguments, making redirection possible
import sys

# Initiates our input array of arguments
input = ""


for arg in sys.stdin:
    input = "".join(arg)


# Sets our key to open a file in the current directory
file_object = open("key",'r')
#Then takes said key and puts it all together to one newkey
newkey = "".join(file_object.read())

# Our xor class, because classes are fun!
class xor(object):

    #Constructo
    def __init__ (self, message, key):
        self.key = key;
        self.message = message;

    # Our Cipher Function which takes a message and a key that can be changed
    def XORCIPHER(self, message, key):
        return(''.join((chr)(ord(m) ^ ord(k)) for (m, k) in zip(message,key)))

# Function Calls
XOR = xor(input, newkey)
print XOR.XORCIPHER(input, newkey)
