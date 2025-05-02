#!/usr/bin/python3

n = int(input())
    
enemies = set()

for i in range(n):
    x,y = map(int,input().split())
    enemies.add((x,y))

m = int(input())
    
allies = set()

for i in range(m):
    x,y = map(int,input().split())
    allies.add((x,y))


max_amount_hit = 0

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

checkWithinRadius((2,2))

def checkEnemy(enemy):
    global max_amount_hit
    center_x,center_y = enemy
    corners = {(center_x-2,center_y-2),(center_x+2,center_y-2),(center_x-2,center_y+2),(center_x+2,center_y+2),}
    for x in range(center_x-2,center_x+3):
        for y in range(center_y-2,center_y+3):
            if (x,y) in corners:
                continue
            kills = checkWithinRadius((x,y))
            if kills>max_amount_hit:
                max_amount_hit = kills
    
for e in enemies:
    checkEnemy(e)
print(max_amount_hit)


