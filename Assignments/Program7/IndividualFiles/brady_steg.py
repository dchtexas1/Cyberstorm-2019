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
SENTINEL = ['\x00', '\xff', '\x00', '\x00', '\xff', '\x00']

def set_settings(args):
    settings = {'interval': '1', 'wrapper': '', 'mode': '', 'offset': '0', 'hidden': '', 'method': ''}
    for value in sys.argv:
        arg = value[0:2]
        if arg == '-b':
            settings['method'] = 'bit'
        elif arg == '-B':
            settings['method'] = 'byte'
        elif arg == '-s':
            settings['mode'] = 'store'
        elif arg == '-r':
            settings['mode'] = 'retrieve'
        elif arg == '-o':
            settings['offset'] = value[2:]
        elif arg == '-i':
            settings['interval'] = value[2:]
        elif arg == '-w':
            settings['wrapper'] = value[2:]
        elif arg == '-h':
            settings['hidden'] = value[2:]
    return settings


def file_to_binary(f, mode="str"):
    """reads each bit of a file and converts to binary string"""
    byte = f.read(1)
    bytes_list = []
    while byte != '':
        bytes_list.append(ord(byte) if mode=="int" else byte) # add each byte into the byte list
        # b += bin(int(binascii.hexlify(byte), 16))[2:].zfill(8)
        byte = f.read(1)
    return bytes_list


def binary_to_ascii(b_string):
    return binascii.unhexlify(('%x' % int(b_string, 2)).zfill(len(b_string) / 4))

def byte_method_retrieve(settings, sentinel):
    wrapper_bytes = get_file_bytes(settings['wrapper'])
    hidden_bytes = []
    offset = int(settings['offset'])
    interval = int(settings['interval'])

    i = 0
    last_six = []
    while last_six != sentinel:
        hidden_bytes.append(wrapper_bytes[offset])
        offset += interval
        i += 1
        if len(hidden_bytes) >= 6:
            last_six = hidden_bytes[-6:]
    return hidden_bytes[:-6]
    
def byte_method_store(settings, sentinel):
    wrapper_bytes = get_file_bytes(settings['wrapper'])
    hidden_bytes = get_file_bytes(settings['hidden']) + sentinel
    offset = int(settings['offset'])
    interval = int(settings['interval'])
    
    i = 0
    while i < len(hidden_bytes):
        wrapper_bytes[offset] = hidden_bytes[i]
        offset += interval
        i += 1
    return wrapper_bytes

# I think this should work, but retrieve method will have to be written
def bit_method_store(settings, sentinel):
    sentinel = [ord(i) for i in sentinel]
    wrapper_bytes = get_file_bytes(settings['wrapper'], 'int')
    hidden_bytes = get_file_bytes(settings['hidden'], 'int') + sentinel
    offset = int(settings['offset'])
    interval = int(settings['interval'])

    i = offset
    j = 0
    while j < len(hidden_bytes):
        for k in range(7):
            wrapper_bytes[i] &= 0b11111110
            wrapper_bytes[i] |= ((hidden_bytes[j] & 0b10000000) >> 7)
            hidden_bytes[j]  << 1
            i += interval
        j += 1

    wrapper_bytes = [chr(i) for i in wrapper_bytes]
    return wrapper_bytes

# still a work in progress
def bit_method_retrieve(settings, sentinel):
    print('starting...')
    sentinel = [ord(i) for i in sentinel]
    wrapper_bytes = get_file_bytes(settings['wrapper'], "int")
    hidden_bytes = []
    offset = int(settings['offset'])
    interval = int(settings['interval'])

    i = offset
    j = 0
    last_six = []
    # This still needs to be written
    while last_six != sentinel:
        hidden_bytes.append(0b0)
        for k in range(7):
            lsb = wrapper_bytes[i] & 1
            hidden_bytes[j] = (hidden_bytes[j] & ~1) | lsb
            i += 1
        if len(hidden_bytes) >= 6:
            last_six = hidden_bytes[-6:]

        print(last_six)
        j += 1

    # hidden_bytes = [chr(i) for i in hidden_bytes]
    return hidden_bytes
'''
def bit_method(settings, sentinel):
    wrapper_bytes = get_file_bytes(settings['wrapper'])
    hidden_bytes = get_file_bytes(settings['hidden']) + sentinel
    offset = int(settings['offset'])
    interval = int(settings['interval'])

    j = 0
    while j < len(hidden_bytes):
        

'''        

def get_file_bytes(f, mode="str"):
    if f == '':
        raise ValueError('file cannot name cannot be empty')
    wrapper_file = open(f, 'rb')
    return file_to_binary(wrapper_file, mode)


    
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
if settings['method'] == 'byte' and settings['mode'] == 'store':
    output = byte_method_store(settings, SENTINEL)
elif settings['method'] == 'byte' and settings['mode'] == 'retrieve':
    output = byte_method_retrieve(settings, SENTINEL)
elif settings['method'] == 'bit' and settings['mode'] == 'store':
    output = bit_method_store(settings, SENTINEL)
elif settings['method'] == 'bit' and settings['mode'] == 'retrieve':
    output = bit_method_retrieve(settings, SENTINEL)



sys.stdout.write("".join([str(b) for b in output]))
