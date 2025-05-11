from collections import defaultdict
from collections import deque
import sys

sys.setrecursionlimit(10**6)

'''
How to make it faster:
Prayer
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
def smallbfs(source, totalTimeSteps, road_list):
    reachable = set()
    queue = deque([(source, 0)])
    while queue:
        u, t = queue.popleft()
        if (u, t) in reachable: continue
        reachable.add((u, t))

        # For every edge out of u
        for (startNode, endNode, _, time) in road_list:
            if startNode == u and t + time <= totalTimeSteps:
                if (endNode, t + time) not in reachable:
                    queue.append((endNode, t + time))
        
        # Allow "wait" edge
        if t + 1 <= totalTimeSteps:
            queue.append((u, t + 1))
    return reachable

def bfs(graph,src,dest,time,usedTime,mincap=0): # returns path to dest or reachable set
    parent = {src:src}
    queue = deque([src])
    while queue:
        UpperNode = queue.popleft()
        for internalNode,cap in graph[UpperNode].items():
            if cap[0] > mincap and internalNode not in parent and time >= usedTime: #and destination
                parent[internalNode] = UpperNode
                queue.append(internalNode)
                if internalNode == dest:
                    p =  []
                    current_vertex = dest
                    while src != current_vertex:
                        p.append((parent[current_vertex],current_vertex))
                        current_vertex = parent[current_vertex]
                    return (True,p)
    return (False,set(parent))
   

def flow(graph, src, dest, totalTime, maxcapacity, numberOfPeople):
    current_flow = 0
    mincap = maxcapacity#1 << (maxcapacity.bit_length() - 1) if maxcapacity > 0 else 0# set to 0 to disable capacity scaling
    while True: #Path is found in each loop
        ispath, p_or_seen = bfs(graph,src,dest,totalTime,0,mincap)
        #ispath, p_or_seen = dfs(graph,src,dest,mincap, set(), totalTime,0)
        if not ispath:
            if mincap > 0:
                mincap = mincap // 2 #Devides by 2 and rounds down, floordivision
                continue
            else:

                return (current_flow,
                        None,
                        None)
        
        #print("path:", *reversed(p_or_seen))
        saturation = min( graph[u][v] for u,v in p_or_seen )
        current_flow += saturation[0]

        if current_flow == numberOfPeople:
            return (current_flow,
                        None,
                        None)
        
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
    
    graph = dict()

    maxcapacity = 0

    road_list = [(0,0,0,0)]*numberOfRoads
    for i in range(numberOfRoads):
        startNode, endNode, people, time = map(int, input().split())
        road_list[i] = (startNode, endNode, people, time)

    reachable = smallbfs(source,totalTimeSteps,road_list)
    
    for i in range(numberOfRoads):
        startNode, endNode, people, time = road_list[i]
        for d in range(totalTimeSteps+1):
            if d + time <= totalTimeSteps and (startNode, d) in reachable and (endNode, d + time) in reachable:
                if (startNode, d) not in graph:
                    graph[(startNode, d)] = dict()
                if (endNode,(d + time)) not in graph:
                    graph[(endNode,(d + time))] = dict()
                graph[(startNode,d)][(endNode,(d + time))] = (people,time)
                maxcapacity = max(maxcapacity,people)
    
    '''
    Use complex numbers to create edges that match the given timestep
    '''

    sink = nodes+1 #Works now
    graph[(sink,-1)] = dict()

    for h in hospitals:
        for d in range(totalTimeSteps+1):
            if (h,d) not in graph:
                    graph[(h,d)] = dict()
            graph[(h,d)][(sink,-1)] = (101,0) #All hospitals have a path to the sink with unlimited space and no time cost.


    #Make a pillar of sink nodes, each one points downward towards th future one, 
    # with people 101 and time 0, that way we make a final node for all

    
    for d in range(totalTimeSteps+1):
        if (source,d) not in graph:
            graph[(source,d)] = dict()
        if (source,(d+1)) not in graph:
            graph[(source,(d+1))] = dict()
        graph[(source,d)][(source,(d+1))] = (101,0)
    
    '''
    for d in range(totalTimeSteps+1):
        graph[(source,0)].update(graph[(source,d)])
    '''

    #print({k: {kk: str(vv) for kk, vv in v.items()} for k, v in graph.items()})

    flow_value, _, _ = flow(graph, (source,0), (sink,-1),totalTimeSteps, maxcapacity, numberOfPeople)

    #print(flow_value)

    #Actual ##print
    
    if flow_value > numberOfPeople:
        print(numberOfPeople)
    else:
        print(flow_value)
    
    

for t in range(amountOfTestcases):
    program()