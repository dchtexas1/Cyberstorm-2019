from pynput.keyboard import Key, Controller
from time import sleep
from random import uniform
from termios import tcflush, TCIFLUSH
from sys import stdin, stdout
import sys

# Things we might want to change
DELAY = 7 # delay before starts typing
OUTPUT = True

def log(s):
  if OUTPUT:
    print(s)

if sys.stdin.isatty():
    sys.stdout.write("Program needs stdin\n")
    exit()

keyboard = Controller()
password = raw_input()
timings = raw_input()


password = password.split(",")
password = password[:len(password) / 2 + 1]
password = "".join(password)


timings = timings.split(",")
timings = [float(a) for a in timings]
keypress = timings[:len(timings) / 2 + 1]
keyinterval = timings[len(timings) / 2 + 1:]


log("Password = {}".format(password))
log("Timings = {}".format(timings))
log("Key press time  = {}".format(keypress))
log("Key intervals = {}".format(keyinterval))


for i in range(DELAY):
  log("staring in {}...".format(DELAY - i))
  sleep(1)

log("Starting...")

i = 0
for char in password:
    keyboard.press(char)
    sleep(keypress[i])
    keyboard.release(char)
    if(i != len(keyinterval)):
        sleep(keyinterval[i])
    i = i + 1

tcflush(stdout,TCIFLUSH)
print
