import math, sys
sys.setrecursionlimit(1000000000)
n = int(input())
distances = []

#yes, ik my variable names suck, but please bear with me
def buildTable(m):
    rows, cols = (1000, m)
    arr = [[0 for _ in range(cols)] for _ in range(rows)]#step,current
    arr[distances[m-1]][m-1] = distances[m-1]
    next = set()
    next.add((distances[m-1]))
    for x in range(m-2,0,-1):
        new = set()
        for smth in next:
            if arr[smth+distances[x]][x]==0 or arr[smth+distances[x]][x]>max(smth+distances[x],arr[smth][x+1]) :
                arr[smth+distances[x]][x] = max(smth+distances[x], arr[smth][x+1])
            new.add(smth+distances[x])
            if smth-distances[x]>=0:
                if  arr[smth-distances[x]][x]==0 or arr[smth-distances[x]][x]>smth:
                    arr[smth-distances[x]][x] = arr[smth][x+1]
                new.add(smth-distances[x])
        next = new
    return arr



for _ in range(n):
    global arr
    m = int(input())
    distances = list(map(int, input().strip().split()))
    arr = buildTable(m)
    start = arr[distances[0]][0]
    checkNext = set()
    checkNext.add((0,""))
    answer = ""
    justStop = False
    for x in range(1,m):
        if justStop:
            break
        min = math.inf
        letsSee = set()
        for smth in checkNext:
            if arr[smth[0]+distances[x-1]][x] != 0:
                if min>arr[smth[0]+distances[x-1]][x]:
                    letsSee.clear()
                    min = arr[smth[0]+distances[x-1]][x]
                    letsSee.add((smth[0]+distances[x-1],smth[1]+"U"))
                elif min == arr[smth[0]+distances[x-1]][x]:
                    letsSee.add((smth[0]+distances[x-1],smth[1]+"U"))
            if smth[0]-distances[x-1]>=0:
                if arr[smth[0]-distances[x-1]][x] !=0:
                    if min>arr[smth[0]-distances[x-1]][x]:
                        letsSee.clear()
                        min = arr[smth[0]-distances[x-1]][x]
                        letsSee.add((smth[0]-distances[x-1],smth[1]+"D"))
                    elif min == arr[smth[0]-distances[x-1]][x]:
                        letsSee.add((smth[0]+distances[x-1],smth[1]+"D"))
        if len(letsSee)==0:
            justStop = True
            break
        elif len(letsSee)==1:
            save = 0
            for uh in letsSee:
                answer += uh[1]
                save = uh[0]
            letsSee.clear()
            letsSee.add((save,""))
            
        checkNext = letsSee
    min = math.inf
    found = False
    if justStop:
        print("IMPOSSIBLE")
    else:
        for uhhh in checkNext:
            if uhhh[0]==distances[m-1]:
                found = True
                answer += "D"
                print(answer)
                break
        if not found:
            print("IMPOSSIBLE")

    
                    






   