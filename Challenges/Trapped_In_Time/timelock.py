##############################################################################
# GitHub Repo Link: https://github.com/dchtexas1/Cyberstorm-2019
# https://github.com/dchtexas1/Cyberstorm-2019/tree/master/Assignments/Program5
#
# CSC 442
# Date: 04/30/19
# Team Name: Romans
# Names: Brady Anderson, Sam Dominguez, Dax Henson, Michael McCrary,
#        Daniel Munger, Stephanie Niemiec, Holland Wolf
#
# Description: Implements timelock algorithm and returns hash for given epoch time 
#              and current system time.  Setting TEST to True allows a hard coded
#              current time to be used, instead of system time.
# 
#
# Run Instructions: python timelock.py < [epoch_time]
#
##############################################################################
from hashlib import md5
from datetime import datetime
import sys
# this is a timezone library that will help convert to UTC
import pytz # NOTE: pip install pytz

TEST = True
TEST_CURRENT_TIME = "2018 04 27 10 00 00" # This needs to be updated for challenge

def get_four_char_hash(h):
    print(h, h[len(h)/2], "<-- I think this is the middle character")
    """hash contains first two alpha characters when read left to right and first two digits when read right to left"""
    alphas = [c for c in h if c.isalpha()]
    digits = [c for c in h if c.isdigit()]
    return "".join(alphas[0:2] + digits[:-3:-1])


def hash(time):
    """returns double md5 hash of input"""
    return md5(md5(str(time)).hexdigest()).hexdigest()

def seconds_since(epoch_time, current_time):
  """returns seconds since epoch and current.  Times must be datetime data type"""
  local = pytz.timezone ("America/Chicago")
  # convert epoch to UTC
  epoch_local_dt = local.localize(epoch_time, is_dst=None)
  epoch_utc_dt = epoch_local_dt.astimezone(pytz.utc)
  # convert current to UTC
  current_local_dt = local.localize(current_time, is_dst=None)
  current_utc_dt = current_local_dt.astimezone(pytz.utc)
  # get difference and round down to interval
  time_diff = int((current_utc_dt - epoch_utc_dt).total_seconds())
  return time_diff - (time_diff % 60)

# ---- Main -----
# exit if standard in is empty
if sys.stdin.isatty():
    sys.stdout.write("Program needs input\n")
    exit()

# save standard in as epoch string
lines = []
for line in sys.stdin:
  lines.append(line)
epoch_str = lines[0].strip()

# save epoch and current time as datetime data structures
epoch_time = datetime.strptime(epoch_str, "%Y %m %d %H %M %S")
current_time = datetime.strptime(TEST_CURRENT_TIME, "%Y %m %d %H %M %S") if TEST else datetime.now()

# get time difference, hash, then print out modified hash
time_diff = seconds_since(epoch_time, current_time)
time_hash = hash(time_diff)
print get_four_char_hash(time_hash)
