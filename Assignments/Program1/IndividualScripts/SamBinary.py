# Team Name: Romans
# Github: 
# Date: 

import sys

# function to split up binary string into 7 or 8 bits
def splitUp(string,length):
        return ' '.join(string[i:i+length] for i in range(0,len(string),length))
    
# takes in input from stdin 
binary = raw_input("")

# converts input to a more user friendly form
sevenBit = splitUp(binary,7) 
eightBit = splitUp(binary,8)


# array to be used later
eightBitChars = []
sevenBitChars = []

# counter

i=0

# conversion for 7 bit ascii converson
# converts the strings to integers
# then converts integers to chars
while(i<len(sevenBit)):
      integer = int((sevenBit[i:i+7]),2)
      sevenBitChars.append(chr(integer))   
      i+=8

i=0
# conversion for 8 bit ascii conversion
# converts the strings to integers
# then converts integers to chars
while(i<len(eightBit)):
    integer = int((eightBit[i:i+8]),2)
    eightBitChars.append(chr(integer))
    i+=9

# output for 7 bit ascii
print "7-Bit ASCII: ",

# writes out the text to stdout
for x in sevenBitChars:
    sys.stdout.write(x)

# new line for formatting purposes
print ""

# output for 8 bit ascii
print "8-Bit ASCII: ",

# writes out the text to stdout
for x in eightBitChars:
    sys.stdout.write(x)

# new line for formatting purposes
print ""

