##########################################################################
# GitHub Repo Link: https://github.com/dchtexas1/Cyberstorm-2019
# GitHub Assignment Link: https://github.com/dchtexas1/Cyberstorm-2019/tree/master/Assignments/Program1
#
# CSC 442
# Date: 03/27/19
# Team Name: Romans
# Names: Brady Anderson, Sam Dominguez, Dax Henson, Michael McCrary,
#        Daniel Munger, Stephanie Niemiec, Holland Wolf
# 
# Description: The purpose of this program is to take a binary value and
#              convert/decode/translate it into ASCII
# 
#              The program identifies whether the provided data is 7-bit
#              or an 8-bit binary input
#
#              The program should identify the following:
#              > When binary input is either 7-bit or 8-bit
#                   -> Error handling if neither
#
#              > Identify if backspaces are included in a binary input
#
# Run Instructions: python Binary.py < {input}
#
#######################################################################
import sys

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
        sys.stdout.write("binary string does not appear to be 7 or 8-bit ASCII. Unable to decode.\n")
    else:
        if len(b_str) % 8 == 0:
            sys.stdout.write("8-bit Binary to ASCII:\n" + binary_decode_by_bit(b_str, 8) + "\n")
        if len(b_str) % 7 == 0:
            sys.stdout.write("7-bit Binary to ASCII:\n" + binary_decode_by_bit(b_str, 7) + "\n")


# MAIN - reads each line of files and converts binary to ASCII
# check if stdin is empty, exit if so
if sys.stdin.isatty():
    sys.stdout.write("Program needs input\n")
    exit()

for line in sys.stdin:
    binary_decode(line)