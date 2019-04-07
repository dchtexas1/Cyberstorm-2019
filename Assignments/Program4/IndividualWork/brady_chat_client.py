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
# Description: Decodes covert messages hidden in file permissions of FTP
#
# Run Instructions: python fetch.py
#
##############################################################################
import sys
import socket

class BinaryDecoder(object):
    def __init__(self):
        pass

    def decode(self, b_str, ascii_length):
        """Return ASCII value of binary string"""
        b_str = str(b_str).strip()
        # remove extra bits if not properly divisible
        b_str = b_str[0:len(b_str) - len(b_str) % ascii_length]
        if not self.check_string(b_str):
            raise ValueError("Binary string must only consist of 0's or 1's")
        return self.__decode_chars(b_str, ascii_length)

    def check_string(self, string):
        """Return True or False if proper binary string"""
        return set(string).issubset(['0', '1'])

    def binary_to_dec(self, n):
        """Convert binary string to integer"""
        return int(n, 2)

    def __decode_chars(self, b_str, ascii_length):
        """Decode binary string based of specified bit length"""
        decoded_chars = []
        temp_str = b_str
        while len(temp_str) > 0:
            to_decode = temp_str[0:ascii_length]
            temp_str = temp_str[ascii_length:]
            decode_dec = self.binary_to_dec(to_decode)
            # check if backspace (backspace is 8 in ASCII)
            if (decode_dec == 8):
                decoded_chars = decoded_chars[:-1]
            else:
                decoded_chars.append(chr(decode_dec))
        return ''.join(decoded_chars)


# ---- MAIN ----
