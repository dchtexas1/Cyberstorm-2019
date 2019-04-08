import socket
import time
from binascii import hexlify
import subprocess

# Covert message and encoding to binary
convert = "Hello World!" + "EOF"
covert_bin = ""
for i in convert:
    covert_bin += bin(int(hexlify(i), 16))[2:].zfill(8)

# Specify length of time for zero or one
ZERO = 0.025
ONE = 0.1

# Overt message
msg = "According to all known laws of aviation, there is no way a bee should be able to fly. Its wings are too small to get its fat little body off the ground. The bee, of course, flies anyway because bees don't care what humans think is impossible. Yellow, black. Yellow, black. Yellow, black. Yellow, black. Ooh, black and yellow! Let's shake it up a little.\n"

c = None

while 1:
    try:
        # start up server
        n = 0
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        port = 1337
        s.bind(("", port))
        s.listen(0)
        print("Listening for client...")
        c, addr = s.accept()
        print("Accepted connection from {}".format(addr))
        # send message overt/covert message
        for i in msg:
            c.send(i)
            if (covert_bin[n] == "0"):
                time.sleep(ZERO)
            else:
                time.sleep(ONE)
            n = (n + 1) % len(covert_bin)
        c.send("EOF")
    except KeyboardInterrupt:
        print ("Shutting down server...")
        break
    except Exception as e:
        print ("Exception: {}".format(e))
        try:
            print('restarting...')
            c.close()
            time.sleep(1)
        except:
            print("Unable to start server, trying again")
            time.sleep(1)

try: 
    c.close()
    print("Server shutdown")
except:
    print("No server created, exiting")
