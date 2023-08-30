def IsNegativeWeightCyclePresent(WL):
    inf = 1 + len(WL.keys()) * max([d for u in WL.keys() for (v,d) in WL[u]])
    distance = dict()
    for v in WL.keys():
        distance[v] = inf

    for i in range(len(WL.keys())+1):
        if(i < len(WL.keys())):
            for u in WL.keys():
                for (v,d) in WL[u]:
                    distance[v] = min(distance[v], distance[u] + d)
        else:
            for u in WL.keys():
                for (v,d) in WL[u]:
                    if(distance[v] > distance[u] + d):
                        return(True)
            return(False)
size = int(input())
edges = eval(input())
WL = {}
for i in range(size):
    WL[i] = []
for ed in edges:
    WL[ed[0]].append((ed[1],ed[2]))
    
print(IsNegativeWeightCyclePresent(WL))