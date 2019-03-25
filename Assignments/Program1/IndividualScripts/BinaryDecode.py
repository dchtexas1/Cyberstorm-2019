#  Daniel Munger
#  Binary Decoder 

# take binary string n and converts to decimal
def binary_to_dec(n):
  # n is binary string, 2 specifies base. In this case base is 2
  return int(n, 2)


# decode binary by specified bit length
def binary_decode_by_bit(b_str, bits):
  decoded_chars = []
  temp_str = b_str
  char_num = 1

  while len(temp_str) > 0:
    # save first n-bits of string
    to_decode = temp_str[0:bits]
    # chop off first n-bits of string
    temp_str = temp_str[bits:]
    # decode character, handle backspace
    decode_dec = binary_to_dec(to_decode)
    print "Encoded Binary Segment {}: {}\t".format(char_num, ''.join(to_decode)) 
    print "Binary Value {}: {}\t".format(char_num, decode_dec)
    print "Decoded Character {}: {}\n".format(char_num, chr(decode_dec))
    char_num = char_num + 1
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
    print("Binary string does not appear to be 7 or 8-bit ASCII. Unable to decode.")
    return
  if len(b_str) % 8 == 0:
    print("8-bit Binary to ASCII:\n" + binary_decode_by_bit(b_str, 8))
  if len(b_str) % 7 == 0:
    print("7-bit Binary to ASCII:\n" + binary_decode_by_bit(b_str, 7))


# MAIN - reads each line of files and converts binary to ASCII
binary_decode("Enter Message Here")
