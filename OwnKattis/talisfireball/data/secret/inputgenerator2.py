import random
import os

people = int(100)
coordinate = int(40)

allies = set()
max_amount_hit = 0
resultOfSquare = set()
enemies = set()

def checkWithinRadius(center):
            counter = 0
            center_x,center_y = center
            corners = {(center_x-2,center_y-2),(center_x+2,center_y-2),(center_x-2,center_y+2),(center_x+2,center_y+2),}
            for x in range(center_x-2,center_x+3):
                for y in range(center_y-2,center_y+3):
                    if (x,y) in corners:
                        continue
                    elif (x,y) in allies:
                        return 0
                    elif (x,y) in enemies:
                        counter+=1
            return counter

def checkEnemy(enemy):
            global max_amount_hit
            global resultOfSquare
            center_x,center_y = enemy
            corners = {(center_x-2,center_y-2),(center_x+2,center_y-2),(center_x-2,center_y+2),(center_x+2,center_y+2),}
            for x in range(center_x-2,center_x+3):
                for y in range(center_y-2,center_y+3):
                    if (x,y) in corners or (x, y) in resultOfSquare:
                        continue
                    kills = checkWithinRadius((x,y))
                    resultOfSquare.add((x,y))
                    if kills>max_amount_hit:
                        max_amount_hit = kills

#!/usr/bin/python3
def checkFile(inputFileName):
    with open(inputFileName+".in", 'r', encoding='utf-8') as file:
        n = int(file.readline().strip())
            
        global enemies
        enemies = set()

        for i in range(n):
            x,y = map(int,file.readline().strip().split())
            enemies.add((x,y))

        m = int(file.readline().strip())
            
        global allies
        allies = set()

        for i in range(m):
            x,y = map(int,file.readline().strip().split())
            allies.add((x,y))


        global max_amount_hit
        global resultOfSquare
        max_amount_hit = 0
        resultOfSquare = set()
            
        for e in enemies:
            if max_amount_hit == 21:
                break
            checkEnemy(e)
        
        answerFile = open(nameOfFile+".ans", "w")
        answerFile.writelines(str(max_amount_hit))
        



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
    nameOfFile = f"testing{x+1}" 
    f = open(nameOfFile+".in", "w")
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
    f.close()
    
    checkFile(nameOfFile)