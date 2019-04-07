import socket
import time
from binascii import hexlify

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
port = 1337
s.bind(("", port))
s.listen(0)
c, addr = s.accept()



convert = "Hello World!" + "EOF"
covert_bin = ""
for i in convert:
    covert_bin += bin(int(hexlify(i), 16))[2:].zfill(8)


ZERO = 0.025
ONE = 0.1
msg = "According to all known laws of aviation, there is no way a bee should be able to fly. Its wings are too small to get its fat little body off the ground. The bee, of course, flies anyway because bees don't care what humans think is impossible. " * 20


n = 0
for i in msg:
    print i
    c.send(i)
    if (covert_bin[n] == "0"):
        time.sleep(0.025)
    else:
        time.sleep(0.1)
    n = (n + 1) % len(covert_bin)
c.send("EOF")
c.close()
