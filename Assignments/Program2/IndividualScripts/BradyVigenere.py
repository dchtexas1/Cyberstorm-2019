import sys

class VigenereCipher:
  def __init__(self, process, key):
    self.key = key
    self.key_position = 0
    if process == '-e':
      self.process = "encrypt"
    elif process == '-d':
      self.process = "decrypt"
    else:
      raise Exception("Invalid process argument: " + process  + ". Use -e for encryption, -d for decryption")
    self.alpha, self.alpha_inverse = self.build_alpha_dicts()

  # encodes or decodes string based on state of cipher
  def cipher(self, s):
    s_lower = s.lower()
    char_list = list(s_lower)
    cipher_list = [self.cipher_char(c) for c in char_list]
    self.reset_key_postion()
    return ''.join(cipher_list)

  # encodes or decodes character based on state of cipher
  def cipher_char(self, c):
    if c not in self.alpha:
      return c
    key_char = self.get_current_key_char()
    key_is_upper = key_char.isupper()
    if self.process == "encrypt":
      cipher_val = self.alpha_inverse[(self.alpha[c] + self.alpha[key_char.lower()]) % 26]
    elif self.process == "decrypt":
      cipher_val = self.alpha_inverse[(26 + self.alpha[c] - self.alpha[key_char.lower()]) % 26]
      
    return cipher_val.upper() if key_is_upper else cipher_val

  # encodes or decodes character based on state of cipher
  def get_current_key_char(self):
    key_char = self.key[self.key_position % len(self.key)]
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
