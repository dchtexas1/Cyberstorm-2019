##############################################################################
# GitHub Repo Link: https://github.com/dchtexas1/Cyberstorm-2019
# https://github.com/dchtexas1/Cyberstorm-2019/tree/master/Assignments/Program7
#
# CSC 442
# Date: 05/01/19
# Team Name: Romans
# Names: Brady Anderson, Sam Dominguez, Dax Henson, Michael McCrary,
#        Daniel Munger, Stephanie Niemiec, Holland Wolf
#
# Description: Implements steg algorithm.
#
# Run Instructions: python steg.py -(bB) -(sr) -o<val> [-i<val>] -w<val> [-h<val>]
#
##############################################################################
import binascii, sys

SENTINEL = ['\x00', '\xff', '\x00', '\x00', '\xff', '\x00']

def set_settings(args):
    """returns a dictionary with method, mode, offset, interval, wrapper file, and hidden file information"""
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
        else:
            raise ValueError("Unknown argument ({})".format(value))
    return settings


def get_file_bytes(f, mode="str"):
    """returns a list of the bytes from specified file.  
    Mode can be used to specify whether to return bytes as integers or strings
    """
    if f == '':
        raise ValueError('file cannot name cannot be empty')
    wrapper_file = open(f, 'rb')
    return file_to_binary(wrapper_file, mode)


def file_to_binary(f, mode="str"):
    """reads each byte of a file and return list of bytes"""
    byte = f.read(1)
    bytes_list = []
    while byte != '':
        bytes_list.append(ord(byte) if mode=="int" else byte)
        byte = f.read(1)
    return bytes_list


def byte_method_store(settings, sentinel):
    """store hidden message file using byte method. Returns list of bytes"""
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


def byte_method_retrieve(settings, sentinel):
    """retrieve hidden message from stegged file using byte method. Returns list of bytes"""
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


def bit_method_store(settings, sentinel):
    """store hidden message file using bit method. Returns list of bytes"""
    sentinel = [ord(i) for i in sentinel]
    wrapper_bytes = get_file_bytes(settings['wrapper'], 'int')
    hidden_bytes = get_file_bytes(settings['hidden'], 'int') + sentinel
    offset = int(settings['offset'])
    interval = int(settings['interval'])

    i = offset
    j = 0
    while j < len(hidden_bytes):
        for k in range(8):
            wrapper_bytes[i] &= 0b11111110
            wrapper_bytes[i] |= ((hidden_bytes[j] & 0b10000000) >> 7)
            hidden_bytes[j] = hidden_bytes[j]  << 1
            i += interval
        j += 1

    wrapper_bytes = [chr(i) for i in wrapper_bytes]
    return wrapper_bytes


def bit_method_retrieve(settings, sentinel):
    """retrieve hidden message from stegged file using bit method. Returns list of bytes."""
    sentinel = [ord(i) for i in sentinel]
    wrapper_bytes = get_file_bytes(settings['wrapper'], "int")
    hidden_bytes = []
    offset = int(settings['offset'])
    interval = int(settings['interval'])

    i = offset
    j = 0
    last_six = []
    while last_six != sentinel:
        hidden_bytes.append(0b0)
        for k in range(8):
            hidden_bytes[j] = hidden_bytes[j] << 1
            lsb = wrapper_bytes[i] & 1
            hidden_bytes[j] = (hidden_bytes[j] & ~1) | lsb
            i += interval
        if len(hidden_bytes) >= 6:
            last_six = hidden_bytes[-6:]
        j += 1
    hidden_bytes = [chr(i) for i in hidden_bytes]
    return hidden_bytes[:-6]    


# ----- Main -----
settings = set_settings(sys.argv)

if settings['method'] == 'byte' and settings['mode'] == 'store':
    output = byte_method_store(settings, SENTINEL)
elif settings['method'] == 'byte' and settings['mode'] == 'retrieve':
    output = byte_method_retrieve(settings, SENTINEL)
elif settings['method'] == 'bit' and settings['mode'] == 'store':
    output = bit_method_store(settings, SENTINEL)
elif settings['method'] == 'bit' and settings['mode'] == 'retrieve':
    output = bit_method_retrieve(settings, SENTINEL)
else:
    Exception("Please include method (-b or -B) and mode (-s or -r) arguments")

sys.stdout.write("".join([str(b) for b in output]))