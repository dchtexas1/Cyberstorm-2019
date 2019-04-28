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

class BinaryDecoder(object):
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
        print(len(b_str))
        print(ascii_length)
        while len(temp_str) > 0:
            to_decode = temp_str[0:ascii_length]
            temp_str = temp_str[ascii_length:]
            decode_dec = self.binary_to_dec(to_decode)
            decoded_chars.append(chr(decode_dec))
        return "".join(decoded_chars)

def ascii_to_binary(a_string):
  return bin(int(binascii.hexlify(a_string), 16))[2:].zfill(len(a_string) * 8)

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
key_f = open('key', 'rb').read()
key_bin = ascii_to_binary(key_f)
bd = BinaryDecoder()

file_bin = ""
for line in sys.stdin:
  file_bin += ascii_to_binary(line)
modified_key_bin = match_length(key_bin, len(file_bin))
xored_bin = xor(file_bin, modified_key_bin)
xor_ascii = bd.decode(xored_bin, 8)
sys.stdout.write(xor_ascii)
