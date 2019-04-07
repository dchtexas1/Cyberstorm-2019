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
from ftplib import FTP

# Variables for Dr. Gourd
# 0 - 7 bits, ignore files with any 1's in first 3; 1 - 10-bits, concatenate
mode = 0
ftp_address = "jeangourd.com"
dir_location = "/"
# NOTE: binary_length is the length of binary (7 or 8) at decode
# it is not number of permissions to reference. 
# For all tests from jeangourd.com, keep at 7
binary_length = 7

# we don't need this for jeangourd.com, but maybe this will be useful later
ftp_username = "anonymous"
ftp_password = ""

class BinaryDecoder(object):
    def __init__(self):
        pass

    def binary_decode(self, b_str, ascii_length):
        """Return ASCII value of binary string"""
        b_str = str(b_str).strip()
        # remove extra bits if not properly divisible
        b_str = b_str[0:len(b_str) - len(b_str) % ascii_length]
        if not self.check_b_string(b_str):
            raise ValueError("Binary string must only consist of 0's or 1's")
        return self.__binary_decode_chars(b_str, ascii_length)

    def check_b_string(self, string):
        """Return True or False if proper binary string"""
        return set(string).issubset(['0', '1'])

    def binary_to_dec(self, n):
        """Convert binary string to integer"""
        return int(n, 2)

    def __binary_decode_chars(self, b_str, ascii_length):
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


# ---- FTP COVERT CHANNEL FUNCTIONS ----
# run perm_single_binary on each and join back into string
def ftp_perm_binary(perm_str):
    return "".join([perm_single_binary(p) for p in list(perm_str)])

# if the characters in the variable 'binary' are a '-' set them '0', else '1'
def perm_single_binary(p):
    return "0" if p == "-" else "1"

# change FTP directory, returns true if success, false if fails
def ftp_navigate(ftp, route):
    for directory in route.split('/'):
        try:
            ftp.cwd(directory)
        except:
            sys.stdout.write("Directory was not found: {} (route: {})\n"
                .format(directory, route))
            return False
    return True

# returns a list of each line of ftp.retrlines.
# this includes files name, size, permissions, etc.
def get_cwd_lines(ftp):
    ls = []
    ftp.retrlines('LIST', ls.append)
    return ls
# ---- END FTP COVERT CHANNEL FUNCTIONS ----


# ---- MAIN ----
# login to the FTP
# ftp = FTP(ftp_address)
# ftp.login(ftp_username, ftp_address)
# # change directories, exit if fails
# if not ftp_navigate(ftp, dir_location):
#     exit()

# # grab files/permission string from directory from FTP, save in list
# ls = get_cwd_lines(ftp)
# b_str = ""
# # convert files permissions based on mode specified
# for line in ls:
#     # mode 0: 7-bit, skip if contains 1's in first 3 permissions
#     if (mode == 0):
#         binary = "" if (ftp_perm_binary(
#             line[0:3]) != "000") else ftp_perm_binary(line[3:10])
#     # mode 1: 10-bit
#     elif (mode == 1):
#         binary = ftp_perm_binary(line[0:10])
#     else:
#         sys.stdout.write("Invalid Mode Selected\n")
#         exit()
#     b_str += binary

# b_str_extra_bits = len(b_str) % binary_length
# b_string_trunc = b_str[0:len(b_str) - b_str_extra_bits]
# binary_decode(b_string_trunc)
b7 = "100100011001011101100110110011011110100000101011111011111110010110110011001000100001"
b8 = "010010000110010101101100011011000110111100100000010101110110111101110010011011000110010000100001"
bb = "111010111100111100101111001001110101110010110111111011111110100010000011100001100001111001111100110111010110000111100111110100111001011011111101110110111111011011111001000100011001011110010"
bd = BinaryDecoder()
# print bd.check_b_string(b7)
print bd.binary_decode(b7, 7)
print bd.binary_decode(b8, 8)
print bd.binary_decode(bb, 7)

