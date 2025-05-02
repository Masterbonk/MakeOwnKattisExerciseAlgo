import random

people = int(100000)
coordinate = int(1000)


def generateCoordinates(coordinate):
    next = True
    while next: 
        x = random.randint(0,coordinate)
        y = random.randint(0,coordinate)
        if (x,y) not in usedSpaces:
            f.writelines(str(x) + " " + str(y) + '\n')
            usedSpaces.add((x,y)) 
            next = False


for x in range(0,1):
    f = open(f"FilledWithAllies2.in", "w")
    """f = open(f"MaxAllies{x+1}.in", "w")"""
    #n = random.randint(1,people)
    #m = random.randint(1,people)
    #m = 0
    n = int(people/2)
    m = int(people/2)
    f.writelines(str(n)+ '\n')
    usedSpaces = set()
    for _ in range(n):
        generateCoordinates(coordinate)
    f.writelines(str(m)+ '\n')
    for _ in range(m):
        generateCoordinates(coordinate)




