##############################################################################
# GitHub Repo Link: https://github.com/dchtexas1/Cyberstorm-2019
# https://github.com/dchtexas1/Cyberstorm-2019/tree/master/Assignments/Program7
#
# CSC 442
# Date: 04/25/19
# Team Name: Romans
# Names: Brady Anderson, Sam Dominguez, Dax Henson, Michael McCrary,
#        Daniel Munger, Stephanie Niemiec, Holland Wolf
#
# Description: Implements steg algorithm.
#
# Run Instructions: python steg.py -(bB) -(sr) -o<val> [-i<val>] -w<val> [-h<val>]
#
##############################################################################
import binascii
import string
import sys

# hardcode the sentinel
# SENTINEL = "00000000 11111111 00000000 00000000 11111111 00000000".replace(' ', '')
SENTINEL = [0x0, 0xff, 0x0, 0x0, 0xff, 0x0]

def set_settings(args):
    settings = {'interval': '', 'wrapper': '', 'mode': '', 'offset': '', 'hidden': '', 'method': ''}
    for value in sys.argv:
        arg = value[0:2]
        if arg == '-b':
            settings['method'] = 'bit'
        elif arg == '-B':
            settings['method'] = 'byte'
        elif arg == '-s':
            settings['mode'] = 'store'
        elif arg == '-r':
            settings['mode'] = 'hide'
        elif arg == '-o':
            settings['offset'] = value[2:]
        elif arg == '-i':
            settings['interval'] = value[2:]
        elif arg == '-w':
            settings['wrapper'] = value[2:]
        elif arg == '-h':
            settings['hidden'] = value[2:]
    return settings


def file_to_binary(f):
    """reads each bit of a file and converts to binary string"""
    byte = f.read(1)
    bytes_list = []
    while byte != '':
        bytes_list.append(byte) # add each byte into the byte list
        # b += bin(int(binascii.hexlify(byte), 16))[2:].zfill(8)
        byte = f.read(1)
    return bytes_list


def binary_to_ascii(b_string):
    return binascii.unhexlify(('%x' % int(b_string, 2)).zfill(len(b_string) / 4))
    
def byte_method_store(settings, sentinel):
    wrapper_bytes = get_file_bin(settings['wrapper'])
    hidden_bytes = get_file_bin(settings['hidden']) + sentinel
    offset = int(settings['offset'])
    interval = int(settings['interval'])
    
    i = 0
    while i < len(hidden_bytes):
        wrapper_bytes[offset] = hidden_bytes[i]
        offset += interval
        i += 1
    return wrapper_bytes

'''
def bit_method(settings, sentinel):
    wrapper_bytes = get_file_bin(settings['wrapper'])
    hidden_bytes = get_file_bin(settings['hidden']) + sentinel
    offset = int(settings['offset'])
    interval = int(settings['interval'])

    j = 0
    while j < len(hidden_bytes):
        

'''        

def get_file_bin(f):
    if f == '':
        raise ValueError('file cannot name cannot be empty')
    wrapper_file = open(f, 'rb')
    return file_to_binary(wrapper_file)


    
'''
def bytemethod():
    #This is just me trying to translate the pseudocode from PDF -Michael
    interval = ((wrapper_size - offset_size)//(hidden_size + sentinel))
    o = offset_size
    S = sentinel
    H = hidden_file
    W = wrapper

    i = 0
    while (i < length(H))
        W[o] = H[i]
        o += I
        i++
        
    i = 0
    while (i < length(S))
        W[o] = S[i]
        o += I
        i++

    

def bitmethod():
    o = offset_size
    I = 1
    S = sentinel
    H = hidden_file
    W = wrapper

    H = H + S
    i = o
    j = 0
    
    # Enhanced for-loop potential here! ( for j in range(length(H))
    while (j < length(H)):
      # Because Python for loops suck
        for k in range(7):
            # Ands Most Significant 7 bits ( We keep the 7 Most Significant Bits)
            W[i] &= 11111110
            # Bitmask to only show most significant bit, then shifting 7 bytes
            W[i] |= ((H[j] & 10000000) >> 7 )
            # Shifts one bit to the left
            H[j] <<= 1
            i = i + I      
        j = j + 1
'''
    
      
      

# ----- Main -----
settings = set_settings(sys.argv)
print settings
# if settings['method'] == 'byte' and settings['mode']:
#     output = byte_method_store(settings, SENTINEL)
# elif settings['method'] == 'bit':
#     output = bit_method_store(settings, SENTINEL)


# print("".join([str(b) for b in output]))
# print (output)
