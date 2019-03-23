import sys

class VigenereCipher(object):
  # constructor for Vigenere Cipher
  def __init__(self, process, key):
    self.process = process
    self.key = key
    self.key_position = 0
    self.alpha, self.alpha_inverse = self.build_alpha_dicts()

  # encodes or decodes string based on state of cipher
  def cipher(self, s):
    # separate all characters in string to list
    char_list = list(s)
    # create a new list using char_list, call cipher_char() on each character
    cipher_list = [self.cipher_char(c) for c in char_list]
    self.reset_key_postion()
    # take the list and merge all the characters into a string
    return ''.join(cipher_list)

  # encodes or decodes character based on state of cipher
  def cipher_char(self, c):
    # if c isn't in alpha (dictionary built in constructor), just return c
    # this is for catching characters like '!' or '#' which are not ciphered
    if c.lower() not in self.alpha:
      return c
    # get current character of key for encoding
    key_char = self.get_current_key_char()
    # save case of c to reference latter
    char_is_upper = c.isupper()
    # preform vigenere cipher encode based on if cipher is set to encrypt or decrypt
    if self.process == "encrypt":
      cipher_val = self.alpha_inverse[(self.alpha[c.lower()] + self.alpha[key_char]) % 26]
    elif self.process == "decrypt":
      cipher_val = self.alpha_inverse[(26 + self.alpha[c.lower()] - self.alpha[key_char]) % 26]
    # return the ciphered value with correct case (upper or lower)
    return cipher_val.upper() if char_is_upper else cipher_val

  # encodes or decodes character based on state of cipher
  def get_current_key_char(self):
    key_char = self.key[self.key_position % len(self.key)]
    # increment key to next position for next access
    self.key_position += 1
    return key_char

  # set key position back to 0
  def reset_key_postion(self):
    self.key_position = 0

  # builds two dictionaries mapping alpha characters to int and another mapping int to alpha
  def build_alpha_dicts(self):
    alpha = {}
    alpha_inverse = {}
    for i in range(26):
      alpha[chr(i + 97)] = i
      alpha_inverse[i] = chr(i + 97)
    return (alpha, alpha_inverse)

  # All functions below are getters and setters class variables
  @property
  def key(self):
    return self._key

  @key.setter
  def key(self, value):
    new_value = value.replace(' ', '').lower()
    if not new_value.isalpha():
      print("Key must only contain alpha values")
      exit()
    self._key = new_value

  @property
  def process(self):
    return self._process

  @process.setter
  def process(self, value):
    if value == '-e':
      process = "encrypt"
    elif value == '-d':
      process = "decrypt"
    else:
      print("Invalid process argument: " + value  + ". Use -e for encryption, -d for decryption")
      exit()
    self._process = process


# Main
if (len(sys.argv) < 3):
  print("Both encode/decode argument and key are required to start cipher")
  exit()

cipher = VigenereCipher(sys.argv[1], sys.argv[2])

while 1:
  try:
    user_input = raw_input('')
    print(cipher.cipher(user_input))
  except EOFError:
    break
