from collections import defaultdict
import sys
sys.setrecursionlimit(10**6)

amountOfTestcases = int(input())

def dfs(graph,u,dest,mincap,seen): # returns path to dest
    if u in seen:
        return (False,seen)
    seen.add(u)
    for v,cap in graph[u].items():
        if cap > mincap: # only consider edges with capacity > mincap
            if v == dest:
                return (True,[(u,v)])
            #print(f'explore {u} {v}, {cap}')
            suc, p = dfs(graph,v,dest,mincap,seen)
            if suc:
                p.append((u,v))
                return (True,p)
    return (False,seen)
   

def flow(orggraph, src,dest):
    graph = defaultdict(lambda: defaultdict(int))
    maxcapacity = 0
    for u,d in orggraph.items():
        for v,c in d.items():
            graph[u][v] = c
            maxcapacity = max(maxcapacity,c)

    current_flow = 0
    mincap = maxcapacity # set to 0 to disable capacity scaling
    while True:
        #ispath, p_or_seen = bfs(graph,src,dest,mincap)
        ispath, p_or_seen = dfs(graph,src,dest,mincap, set())
        if not ispath:
            if mincap > 0:
                mincap = mincap // 2
                continue
            else:
                return (current_flow,
                        { a:{b:c-graph[a][b] for b,c in d.items() if graph[a][b]<c} 
                            for a,d in orggraph.items() },
                        p_or_seen)
        p = p_or_seen
        print("path:", *reversed(p))
        saturation = min( graph[u][v] for u,v in p )
        print(current_flow,saturation)#,[f"{u[0]}-{u[1]}:{orggraph[u[0]][u[1]]}:{graph[u][v]}" for u,v in p if u[2]==0])
        current_flow += saturation
        for u,v in p:
            graph[u][v] -= saturation
            graph[v][u] += saturation

def program():
    nodes = int(input())
    source, numberOfPeople, totalTimeSteps = map(int, input().split(" "))
    numberOfHospital = int(input())
    hospitals = set()
    for i in range(numberOfHospital):
        hospitals.add(int(input()))
    
    numberOfRoads = int(input())
    
    graph = defaultdict(lambda: defaultdict(int))


    for i in range(numberOfRoads):
        startNode, endNode, people, time = map(int, input().split())
        for d in range(totalTimeSteps):
            graph[startNode+d*j][endNode+d+time*j] = people #People,time
    
    '''
    Use imaginary numbers to create edges that match the given timestep
    '''

    print(graph)
    
    sink = nodes+1
    
    for h in hospitals:
        graph[h][sink] = 101#(101,0) #All hospitals have a path to the sink with unlimited space and no time cost.

    flow_value, residual_graph, extra = flow(graph, source, sink)

    print("Own prints")
    print(flow_value)
    print(residual_graph)
    print(extra)
    print()

    

    







for t in range(amountOfTestcases):
    program()