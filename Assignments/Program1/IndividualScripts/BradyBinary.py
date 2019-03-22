import sys

# take binary string n and converts to decimal
def binary_to_dec(n):
  return int(n, 2)


# decode binary by specified bit length
def binary_decode_by_bit(b_str, bits):
  decoded_chars = []
  temp_str = b_str

  while len(temp_str) > 0:
    to_decode = temp_str[0:bits]
    temp_str = temp_str[bits:]
    # decode character, handle backspace
    decode_dec = binary_to_dec(to_decode)
    if (decode_dec == 8):
      decoded_chars = decoded_chars[:-1]
    else:
      decoded_chars.append(chr(decode_dec))

  return ''.join(decoded_chars)


# take binary string and converts to ASCII string
# string length determines if 8-bit length, 7-bit, or both are used for decode
def binary_decode(b_str):
  if (len(b_str) % 8 != 0 and len(b_str) % 7 != 0):
    print("binary string does not appear to be 7 or 8-bit ASCII. Unable to decode.")
    return
  if len(b_str) % 8 == 0:
    print("8-bit Binary to ASCII:\n" + binary_decode_by_bit(b_str, 8))
  if len(b_str) % 7 == 0:
    print("7-bit Binary to ASCII:\n" + binary_decode_by_bit(b_str, 7))


# MAIN - reads each line of files and converts binary to ASCII
for line in sys.stdin:
    binary_decode(line)