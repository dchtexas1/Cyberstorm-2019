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

# ---- BINARY DECODER FUNCTIONS ----
# take binary string n and converts to decimal
def binary_to_dec(n):
    # n is binary string, 2 specifies base. In this case base is 2
    return int(n, 2)

# decode binary by specified bit length
def binary_decode_by_bit(b_str, bits):
    decoded_chars = []
    temp_str = b_str

    while len(temp_str) > 0:
        # save first n-bits of string
        to_decode = temp_str[0:bits]
        # chop off first n-bits of string
        temp_str = temp_str[bits:]
        # decode character, handle backspace
        decode_dec = binary_to_dec(to_decode)
        # check if backspace (backspace is 8 in ASCII)
        if (decode_dec == 8):
            decoded_chars = decoded_chars[:-1]
            # if not backspace, convert int to ASCII and append to char array
        else:
            decoded_chars.append(chr(decode_dec))
            # smash array into string and return
    return ''.join(decoded_chars)

# take binary string and converts to ASCII string
# string length determines if 8-bit length, 7-bit, or both are used for decode
def binary_decode(b_str):
    if (len(b_str) % 8 != 0 and len(b_str) % 7 != 0):
        sys.stdout.write("binary string does not appear to be 7 or 8-bit " \
            "ASCII. Unable to decode.\n")
    else:
        if len(b_str) % 8 == 0:
            sys.stdout.write("8-bit Binary to ASCII:\n{}\n"
                .format(binary_decode_by_bit(b_str, 8)))
        if len(b_str) % 7 == 0:
            sys.stdout.write("7-bit Binary to ASCII:\n{}\n"
                .format(binary_decode_by_bit(b_str, 7)))

# checks if a given string contains only 0's and 1's
def check_b_string(string):
    return set(string).issubset(['0', '1'])

# ---- END BINARY DECODER FUNCTIONS ----


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
ftp = FTP(ftp_address)
ftp.login(ftp_username, ftp_address)
# change directories, exit if fails
if not ftp_navigate(ftp, dir_location):
    exit()

# grab files/permission string from directory from FTP, save in list
ls = get_cwd_lines(ftp)
b_str = ""
# convert files permissions based on mode specified
for line in ls:
    # mode 0: 7-bit, skip if contains 1's in first 3 permissions
    if (mode == 0):
        binary = "" if (ftp_perm_binary(
            line[0:3]) != "000") else ftp_perm_binary(line[3:10])
    # mode 1: 10-bit
    elif (mode == 1):
        binary = ftp_perm_binary(line[0:10])
    else:
        sys.stdout.write("Invalid Mode Selected\n")
        exit()
    b_str += binary

b_str_extra_bits = len(b_str) % binary_length
b_string_trunc = b_str[0:len(b_str) - b_str_extra_bits]
binary_decode(b_string_trunc)
