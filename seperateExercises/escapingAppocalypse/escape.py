from collections import defaultdict
import sys
sys.setrecursionlimit(10**6)

'''
How to make it faster:
'''

amountOfTestcases = int(input())

'''def dfs(graph,node,dest,mincap,seen,time,usedTime): # returns path to dest
    if node in seen:
        return (False,seen)
    seen.add(node)

    for internalNode,cap in graph[node].items():
        internalnode_time = int(internalNode.imag)
        

        if cap[0] > mincap and usedTime <= internalnode_time and time >= usedTime:  # only consider edges with capacity > mincap
            if internalNode == dest:
                return (True,[(node,internalNode)])
            suc, p = dfs(graph,internalNode,dest,mincap,seen,time,usedTime+cap[1])
            if suc:
                p.append((node,internalNode))
                return (True,p)
    return (False,seen)
'''
def bfs(graph,src,dest,time,usedTime,mincap=0): # returns path to dest or reachable set
    parent = {src:src}
    layer = [src]
    while layer:
        nextlayer = []
        for UpperNode in layer:
            for internalNode,cap in graph.get(UpperNode, {}).items():
                internalnode_time = internalNode[1]
                destination = True
                if internalnode_time != -1:
                    if usedTime > internalnode_time:
                        destination = False
                if cap[0] > mincap and internalNode not in parent and destination and time >= usedTime:
                    parent[internalNode] = UpperNode
                    nextlayer.append(internalNode)
                    if internalNode == dest:
                        p =  []
                        current_vertex = dest
                        while src != current_vertex:
                            p.append((parent[current_vertex],current_vertex))
                            current_vertex = parent[current_vertex]
                        return (True,p)
        layer = nextlayer
    return (False,set(parent))
   

def flow(graph, src, dest, totalTime, maxcapacity):
    current_flow = 0
    mincap = maxcapacity # set to 0 to disable capacity scaling
    while True: #Path is found in each loop
        ispath, p_or_seen = bfs(graph,src,dest,totalTime,0,mincap)
        #ispath, p_or_seen = dfs(graph,src,dest,mincap, set(), totalTime,0)
        if not ispath:
            if mincap > 0:
                mincap = mincap // 2 #Devides by 2 and rounds down, floordivision
                continue
            else:

                return (current_flow,
                        { a:{b:c[0]-graph[a][b][0] for b,c in d.items() if graph[a][b]<c} 
                            for a,d in graph.items() },
                        p_or_seen)
        
        #print("path:", *reversed(p_or_seen))
        saturation = min( graph[u][v] for u,v in p_or_seen )
        current_flow += saturation[0]
        for u,v in p_or_seen:
            graph[u][v] = (graph[u][v][0]-saturation[0],graph[u][v][1])
            graph[v][u] = (graph[u][v][0]+saturation[0],graph[u][v][1])

def program():
    nodes = int(input())
    source, numberOfPeople, totalTimeSteps = map(int, input().split(" "))
    numberOfHospital = int(input())
    hospitals = set()
    for i in range(numberOfHospital):
        hospitals.add(int(input()))
    
    numberOfRoads = int(input())
    
    graph = {}

    maxcapacity = 0
    for i in range(numberOfRoads):
        startNode, endNode, people, time = map(int, input().split())
        for d in range(totalTimeSteps+1):
            if d + time <= totalTimeSteps:
                if (startNode, d) not in graph:
                    graph[(startNode, d)] = {}
                if (endNode,(d + time)) not in graph:
                    graph[endNode,(d + time)] = {}
                graph[(startNode,d)][(endNode,(d + time))] = (people,time)
                maxcapacity = max(maxcapacity,people)

    
    '''
    Use complex numbers to create edges that match the given timestep
    '''

    sink = nodes+1 #Works now
    source = source #Correct
    graph[(sink,-1)] = {}
    
    for h in hospitals:
        for d in range(totalTimeSteps+1):
            if (h, d) not in graph:
                    graph[(h, d)] = {}
            graph[(h,d)][(sink,-1)] = (101,0) #All hospitals have a path to the sink with unlimited space and no time cost.


    #Make a pillar of sink nodes, each one points downward towards th future one, 
    # with people 101 and time 0, that way we make a final node for all

    for d in range(totalTimeSteps+1):
        if (source, d) not in graph:
                    graph[(source, d)] = {}
        graph[(source,d)][(source,(d+1))] = (101,0)

    #print({k: {kk: str(vv) for kk, vv in v.items()} for k, v in graph.items()})

    flow_value, residual_graph, extra = flow(graph, (source,0), (sink,-1),totalTimeSteps, maxcapacity)

    #print(flow_value)
    
    if flow_value > numberOfPeople:
        print(numberOfPeople)
    else:
        print(flow_value)
        
    
    #Actual ##print
    

for t in range(amountOfTestcases):
    program()