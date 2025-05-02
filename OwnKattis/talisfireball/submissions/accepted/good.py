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
    center_x,center_y = center
    corners = {(center_x-2,center_y-2),(center_x+2,center_y-2),(center_x-2,center_y+2),(center_x+2,center_y+2),}
    for x in range(center_x-2,center_x+3):
        for y in range(center_y-2,center_y+3):
            if (x,y) in corners:
                continue
            if (x,y) in allies:

checkWithinRadius((2,2))



