#This file validates the input. I makes sure the input matches the given restraint in the excersise
import sys
import re

def checkGroup():
    n = sys.stdin.readline().strip() #Reads the line
    if not re.match(r"^(0|[1-9][0-9]*)$", n): #Checks for actual numbers
        print("first")
        sys.exit(43) #fail
    else:
        try:
            n = int(n) #Turns the line(string) into an int
        except ValueError:
            print("second")
            sys.exit(43) #fail

    for _ in range(n):
        line = sys.stdin.readline()
        if not re.match(r"(0|([1-9][0-9]*)) (0|([1-9][0-9]*))", line): #Checks for actual numbers in the form of x y
            print("third")
            sys.exit(43) #fail
        try:
            x,y = map(int,line.strip().split(" ")) #Turns the line(string) into an int

            if not 0 <= x <= 100000: #Checks the range
                print("fourth")
                sys.exit(43) #fail
            if not 0 <= y <= 100000: #Checks the range
                print("fifth")
                sys.exit(43) #fail
        except ValueError:
            print("sixth")
            sys.exit(43) #fail

checkGroup()
checkGroup()

if sys.stdin.readline() != "": #Checks that there are only the desired amount of inputs
    sys.exit(43) #fail
sys.exit(42) #success