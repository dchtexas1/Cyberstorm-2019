##############################################################################
# GitHub Repo Link: https://github.com/dchtexas1/Cyberstorm-2019
# https://github.com/dchtexas1/Cyberstorm-2019/tree/master/Assignments/Program6
#
# CSC 442
# Date: 04/25/19
# Team Name: Romans
# Names: Brady Anderson, Sam Dominguez, Dax Henson, Michael McCrary,
#        Daniel Munger, Stephanie Niemiec, Holland Wolf
#
# Description: implements XOR crypto for message.
#
# Run Instructions: python xor.py
#
##############################################################################
import binascii, string, sys

def ascii_to_binary(a_string):
  return bin(int(binascii.hexlify(a_string), 16))[2:].zfill(len(a_string) * 8)

def binary_to_ascii(b_string):
  return binascii.unhexlify('%x' % int(b_string, 2))

def file_to_binary(f):
  """reads each bit of a file and converts to binary string"""
  b = ''
  byte = f.read(1)
  while byte!='':
      b += bin(int(binascii.hexlify(byte), 16))[2:].zfill(8)
      byte = f.read(1)
  return b

def match_length(s, length):
  """Extend or tuncate string to match given length"""
  if (length < 1):
    raise ValueError("Length must be 1 or greater")
  bin_len = len(s)
  if (bin_len  > length):
    return s[:length]
  if (bin_len < length):
    length_multiplier = (length / bin_len) + 1
    x = s * length_multiplier
    return (s * length_multiplier)[:length]
  return s

def xor(b_str_1, b_str_2):
  return bin(int(b_str_1, 2) ^ int(b_str_2, 2))[2:].zfill(len(b_str_1))

# ---- Main ----
key_f = open('key', 'rb')
key_bin = file_to_binary(key_f)
  
file_bin = ""
for line in sys.stdin:
  file_bin += ascii_to_binary(line)

modified_key_bin = match_length(key_bin, len(file_bin))
xored_bin = xor(file_bin, modified_key_bin)
xor_ascii = binary_to_ascii(xored_bin)
sys.stdout.write(xor_ascii)
