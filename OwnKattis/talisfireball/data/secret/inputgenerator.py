import random
def generateCoordinates(coordinate):
    next = True
    while next: 
        x = random.randint(0,coordinate)
        y = random.randint(0,coordinate)
        if (x,y) not in usedSpaces:
            f.writelines(str(x) + " " + str(y) + '\n')
            usedSpaces.add((x,y)) 
            next = False


for x in range(4,50):
    f = open(f"file{x+1}.in", "w")
    people = int(100000)
    n = random.randint(1,people)
    m = random.randint(1,people)
    coordinate = int(100000)
    f.writelines(str(n)+ '\n')
    usedSpaces = set()
    for _ in range(n):
        generateCoordinates(coordinate)
    f.writelines(str(m)+ '\n')
    for _ in range(m):
        generateCoordinates(coordinate)




