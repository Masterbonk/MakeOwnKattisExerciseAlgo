from collections import defaultdict
from collections import deque
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
    queue = deque([src])
    while queue:
        UpperNode = queue.popleft()
        for internalNode,cap in graph[UpperNode].items():
            '''destination = True
            if internalNode[1] != -1:
                if usedTime > internalNode[1]:
                    destination = False
            '''
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
                        None,
                        None)
        
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
    
    graph = defaultdict(lambda: defaultdict(int))

    maxcapacity = 0
    for i in range(numberOfRoads):
        startNode, endNode, people, time = map(int, input().split())
        for d in range(totalTimeSteps+1):
            if d + time <= totalTimeSteps:
                graph[(startNode,d)][(endNode,(d + time))] = (people,time)
                maxcapacity = max(maxcapacity,people)
    '''
    Use complex numbers to create edges that match the given timestep
    '''

    sink = nodes+1 #Works now
    source = source #Correct
    
    for h in hospitals:
        for d in range(totalTimeSteps+1):
            graph[(h,d)][(sink,-1)] = (101,0) #All hospitals have a path to the sink with unlimited space and no time cost.


    #Make a pillar of sink nodes, each one points downward towards th future one, 
    # with people 101 and time 0, that way we make a final node for all

    '''
    for d in range(totalTimeSteps+1):
        graph[(source,d)][(source,(d+1))] = (101,0)
    '''
    for d in range(totalTimeSteps+1):
        graph[(source,0)].update(graph[(source,d)])

    #print({k: {kk: str(vv) for kk, vv in v.items()} for k, v in graph.items()})

    flow_value, _, _ = flow(graph, (source,0), (sink,-1),totalTimeSteps, maxcapacity)

    #print(flow_value)

    #Actual ##print
    
    if flow_value > numberOfPeople:
        print(numberOfPeople)
    else:
        print(flow_value)
    
    

for t in range(amountOfTestcases):
    program()