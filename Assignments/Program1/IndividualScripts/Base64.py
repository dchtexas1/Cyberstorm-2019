#  Daniel Munger
#  Base-64 Decoder 

# take binary string n and converts to decimal
def binary_to_dec(n):
  # n is binary string, 2 specifies base. In this case base is 2
  return int(n, 2)


# decode binary by specified bit length
def binary_decode_by_bit(b_str):
  decoded_chars = []
  temp_str = b_str
  char_num = 1

  while len(temp_str) > 0:
    # save first n-bits of string
    to_decode = temp_str[0:6]
    # chop off first n-bits of string
    temp_str = temp_str[6:]
    # decode character, handle backspace
    decode_dec = binary_to_dec(to_decode)
    print "Encoded Binary Segment {}: {}\t".format(char_num, ''.join(to_decode)) 
    print "Binary Value {}: {}\t".format(char_num, decode_dec)
    if (decode_dec < 26):
        print "Decoded Character {}: {}\n".format(char_num, chr(65 + decode_dec))
        decoded_chars.append(chr(65 + decode_dec))
    elif (decode_dec < 52):
        print "Decoded Character {}: {}\n".format(char_num, chr(71 + decode_dec))
        decoded_chars.append(chr(71 + decode_dec))
    elif (decode_dec < 62):
        print "Decoded Character {}: {}\n".format(char_num, chr(71 + decode_dec))
        decoded_chars.append(chr(decode_dec - 4))
    elif (decode_dec == 62):
        print "Decoded Character {}: + \n".format(char_num)
        decoded_chars.append('+')
    else:
        print "Decoded Character {}: / \n".format(char_num)
        decoded_chars.append('/')
    char_num = char_num + 1
  # smash array into string and return
  return ''.join(decoded_chars)


# take binary string and converts to ASCII string
# string length determines if 8-bit length, 7-bit, or both are used for decode
def binary_decode(b_str):
  if (len(b_str) % 6 != 0):
    print("Binary string does not appear to be in base 64. Unable to decode.")
    return
  if len(b_str) % 6 == 0:
    print("6-bit Binary to Base-64:\n" + binary_decode_by_bit(b_str))


# MAIN - reads each line of files and converts binary to ASCII
binary_decode("000111011110100101100101101000")

