#This file validates the input. I makes sure the input matches the given restraint in the excersise
import sys
import re

for _ in range(2):
    line = sys.stdin.readline() #Reads the line
    if not re.match(r"(0|([1-9][0-9]*))\n", line): #Checks for actual numbers
        print("first")
        sys.exit(43) #fail
    try:
        x = int(line) #Turns the line(string) into an int

        if not 0 <= x <= 100: #Checks the range
            print("second")
            sys.exit(43) #fail
    except ValueError:
        print("third")
        sys.exit(43) #fail

if sys.stdin.readline() != "": #Checks that there are only the desired amount of inputs
    sys.exit(43) #fail
sys.exit(42) #success
