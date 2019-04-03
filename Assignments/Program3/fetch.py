##########################################################################
# GitHub Repo Link: https://github.com/dchtexas1/Cyberstorm-2019
# GitHub Assignment Link: https://github.com/dchtexas1/Cyberstorm-2019/tree/master/Assignments/Program3
#
# CSC 442
# Date: 04/02/19
# Team Name: Romans
# Names: Brady Anderson, Sam Dominguez, Dax Henson, Michael McCrary,
#        Daniel Munger, Stephanie Niemiec, Holland Wolf
#
# Description:
#
# Run Instructions: python fetch.py
#
#######################################################################
import sys
from ftplib import FTP

# Variables for Dr. Gourd
mode = 0  # 0 - 7 bits, ignore files with any 1's in first 3; 1 - 10-bits, concatenate
ftp_address = "jeangourd.com"
dir_location = "/"

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
        sys.stdout.write(
            "binary string does not appear to be 7 or 8-bit ASCII. Unable to decode.\n")
    else:
        if len(b_str) % 8 == 0:
            sys.stdout.write("8-bit Binary to ASCII:\n" +
                             binary_decode_by_bit(b_str, 8) + "\n")
        if len(b_str) % 7 == 0:
            sys.stdout.write("7-bit Binary to ASCII:\n" +
                             binary_decode_by_bit(b_str, 7) + "\n")

# checks if a given string contains only 0's and 1's
def check_b_string(string):
    return set(string).issubset(['0', '1'])

# ---- END BINARY DECODER FUNCTIONS ----



# ---- FTP COVERT CHANNEL FUNCTIONS ----
# turn everything into a list, call perm_single_binary, and join everything into a string
def ftp_perm_binary(perm_str):
    return "".join([perm_single_binary(p) for p in list(perm_str)])

# if the characters in the variable 'binary' are a '-' set them '0', else '1'
def perm_single_binary(p):
    return "0" if p == "-" else "1"
# ---- END FTP COVERT CHANNEL FUNCTIONS ----



# ---- MAIN ----
# login to the FTP
ftp = FTP(ftp_address)
ftp.login() # we can add a username a password here if we need

# change to correct directory in FTP
for directory in dir_location.split('/'):
    try:
        ftp.cwd(directory)
    except:
        print("Directory was not found: " + directory + " (route: " + dir_location + ")")
        exit()

# grab files/permission string from directory from FTP, save in list
ls = []
ftp.retrlines('LIST', ls.append)

b_str = ""

for line in ls:
    print("line",line)
    if (mode == 0): # for 7-bits
        # skip decoding if contains any 1's in first 3 permissions
        if (ftp_perm_binary(line[0:3]) != "000"):
            binary = ""            
        else:
            binary = ftp_perm_binary(line[3:10])

    elif (mode == 1): # for 10-bits
        binary = ftp_perm_binary(line[0:10])
    else:
        print("Invalid Mode Selected")
        exit()
    b_str += binary
    
b_str_len = len(b_str)
b_string_trunc = b_str[0:b_str_len - (b_str_len % 7)] # here's another option that does the same thing
# b_string_trunc = b_str[0:](len(b_str) // 7) * 7 # change to string with a length divisible by 7 (there's probably a better way to do this)
binary_decode(b_string_trunc)
