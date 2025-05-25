import math, sys
sys.setrecursionlimit(1000000000)
n = int(input())
distances = []

def buildTable(m):
    rows, cols = (1000, m)
    arr = [[0 for _ in range(cols)] for _ in range(rows)]#step,current
    arr[distances[m-1]][m-1] = distances[m-1]
    next = set()
    next.add((distances[m-1]))
    for x in range(m-2,0,-1):
        new = set()
        for values in next:
            if arr[values+distances[x]][x]==0 or arr[values+distances[x]][x]>max(values+distances[x],arr[values][x+1]) :
                arr[values+distances[x]][x] = max(values+distances[x], arr[values][x+1])
            new.add(values+distances[x])
            if values-distances[x]>=0:
                if  arr[values-distances[x]][x]==0 or arr[values-distances[x]][x]>arr[values][x+1]:
                    arr[values-distances[x]][x] = arr[values][x+1]
                new.add(values-distances[x])
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
        for values in checkNext:
            if arr[values[0]+distances[x-1]][x] != 0:
                if min>arr[values[0]+distances[x-1]][x]:#can you always follow the min?
                    letsSee.clear()
                    min = arr[values[0]+distances[x-1]][x]
                    letsSee.add((values[0]+distances[x-1],values[1]+"U"))
                elif min == arr[values[0]+distances[x-1]][x]:
                    letsSee.add((values[0]+distances[x-1],values[1]+"U"))
            if values[0]-distances[x-1]>=0:
                if arr[values[0]-distances[x-1]][x] !=0:
                    if min>arr[values[0]-distances[x-1]][x]:
                        letsSee.clear()
                        min = arr[values[0]-distances[x-1]][x]
                        letsSee.add((values[0]-distances[x-1],values[1]+"D"))
                    elif min == arr[values[0]-distances[x-1]][x]:
                        letsSee.add((values[0]-distances[x-1],values[1]+"D"))
        if len(letsSee)==0:
            justStop = True
            break
        elif len(letsSee)==1:
            save = 0
            for x in letsSee:
                answer += x[1]
                save = x[0]
            letsSee.clear()
            letsSee.add((save,""))
        else:
            same = True
            prev = (-1,"")
            for value in letsSee:
                if value[0]==prev[0] or prev[0]==-1:
                    prev = value
                else:
                    same = False
                    break
            if same:
                answer += prev[1]
                letsSee.clear()
                letsSee.add((prev[0],""))
            
        checkNext = letsSee
    min = math.inf
    found = False
    if justStop:
        print("IMPOSSIBLE")
    else:
        for x in checkNext:
            if x[0]==distances[m-1]:
                found = True
                answer += "D"
                print(answer)
                break
        if not found:
            print("IMPOSSIBLE")

    
                    






   