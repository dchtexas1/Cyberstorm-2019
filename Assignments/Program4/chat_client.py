##############################################################################
# GitHub Repo Link: https://github.com/dchtexas1/Cyberstorm-2019
# https://github.com/dchtexas1/Cyberstorm-2019/tree/master/Assignments/Program4
#
# CSC 442
# Date: 04/02/19
# Team Name: Romans
# Names: Brady Anderson, Sam Dominguez, Dax Henson, Michael McCrary,
#        Daniel Munger, Stephanie Niemiec, Holland Wolf
#
# Description: Decodes covert messages hidden in timing schemes of overt
# messages on a chat server. Auto detects timing.  See Mode notes below for
# instructions.
#
# Run Instructions: python chat_client.py
#
##############################################################################
import sys, socket, string
from time import time
from collections import Counter

# Server
ip = "jeangourd.com"
port = 31337

# ---- Mode ----
# high refers to longest time delay, low is the shortest
# ex: if time is 0.025 and .100, then .100 is high
# program will auto detect low and high times
# 0 - ZERO (low), ONE (high)
# 1 - ZERO (high), ONE (low)
# 2 - Output results of both mode 1 and 2
MODE = 0

# Other modifications
DEBUG = False # change to true to see timing printout
ASCII_LENGTH = 8
TIME_ACCURACY = 3

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
        while len(temp_str) > 0:
            to_decode = temp_str[0:ascii_length]
            temp_str = temp_str[ascii_length:]
            decode_dec = self.binary_to_dec(to_decode)
            # check if backspace (backspace is 8 in ASCII)
            if (decode_dec == 8):
                decoded_chars = decoded_chars[:-1]
            else:
                decoded_chars.append(chr(decode_dec))
        # remove some printable characters that are not used
        pos_chars = string.printable.replace("\r\x0b\x0c", "")
        # replace nonprintable with "?"
        decoded_chars = [i if i in pos_chars else "?" for i in decoded_chars]
        return ''.join(decoded_chars)

# ---- Chat Client Functions ----
def receive_msg(ip, port, time_accuracy = 3):
    RECV_AMT = 4096
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # create the socket
    s.connect((ip, port)) # connect to the ip and port specified above

    print("[connect to chat server]\n...")
    data = s.recv(RECV_AMT)
    deltas = []
    overt_msg = ""
    last_three_chars = ""
    # receive data loop
    while (data.rstrip("\n") != "EOF" and last_three_chars != "EOF" ):
        overt_msg += data
        sys.stdout.write(data)
        sys.stdout.flush()
        t0 = time()
        data = s.recv(RECV_AMT)
        t1 = time()
        delta = round(t1 - t0, time_accuracy)
        deltas.append(delta)
        # save last three characters to handle EOF hang case
        if len(overt_msg) >= 3:
            last_three_chars = overt_msg[-3:]
    s.close()
    print("...\n[disconnect from the chat server]")
    return deltas

def build_binary_from_deltas(deltas, mode, high, low):
    """take array of delta timing values and translate to binary"""
    return "".join([get_delta_binary_value(delta, mode, high, low) for delta in deltas])

def get_delta_binary_value(delta, mode, high, low):
    """converts delta time value to best guess binary value"""
    if (mode != 0 and mode != 1):
        raise ValueError("Invalid Mode")
    low_bit, high_bit = ("1", "0") if mode == 1 else ("0", "1")
    midpoint = float(high + low) / 2
    if (delta <= midpoint):
        return low_bit
    else:
        return high_bit

def print_debug(deltas):
    print "\n----- START Debug -----"
    print deltas
    print "\n"
    print Counter(deltas)
    print "----- END Debug -----\n"

# ---- MAIN ----
deltas = receive_msg(ip, port, TIME_ACCURACY)
peaks = [i[0] for i in Counter(deltas).most_common(2)]
high, low = max(peaks), min(peaks)

if DEBUG:
    print_debug(deltas)

bd = BinaryDecoder()

# ZERO (low), ONE (high)
if MODE == 0 or MODE == 2:
    msg = bd.decode(build_binary_from_deltas(deltas, 0, high, low), ASCII_LENGTH)
    print "Covert message:",
    print msg.split("EOF")[0]
# ZERO (high), ONE (low)
if MODE == 1 or MODE == 2:
    msg = bd.decode(build_binary_from_deltas(deltas, 1, high, low), ASCII_LENGTH)
    print "Covert message:",
    print msg.split("EOF")[0]
