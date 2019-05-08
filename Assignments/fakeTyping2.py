from pynput.keyboard import Key, Controller
from time import sleep
from random import uniform
from termios import tcflush, TCIFLUSH
from sys import stdin, stdout

keyboard = Controller()
password = raw_input()
timings = raw_input()
print "Password = {}".format(password)
print "Timings = {}".format(timings)

password = password.split(",")
password = password[:len(password) / 2 + 1]
password = "".join(password)

print password
timings = timings.split(",")
timings = [float(a) for a in timings]
keypress = timings[:len(timings) / 2 + 1]
keyinterval = timings[len(timings) / 2 + 1:]

print "Key press time  = {}".format(keypress)
print "Key intervals = {}".format(keyinterval)

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
