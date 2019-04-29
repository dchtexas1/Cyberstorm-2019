from hashlib import md5

def get_four_char_hash(h):
    """hash contains first two alpha characters when read left to right and first two digits when read right to left"""
    alphas = [c for c in h if c.isalpha()]
    digits = [c for c in h if c.isdigit()]
    return "".join(alphas[0:2] + digits[:-3:-1])


def hash(s):
    """returns double md5 hash of input"""
    return md5(md5(s).hexdigest()).hexdigest()

def time_since(start_time, end_time):
    pass