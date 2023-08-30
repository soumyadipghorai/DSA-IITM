def FiberLink(distance_map):
    (edges, component, t, l, s) = (list(), dict(), list(), list(distance_map.keys()), 0)
    for u in l:
        edges.extend((d,u,v) for (v,d) in distance_map[u])
        component[u] = u
    edges.sort()

    for [d,u,v] in edges:
        if(component[u] != component[v]):
            t.append((u,v))
            c = component[u]
            s += d
            for i in l:
                if(component[i] == c):
                    component[i] = component[v]
    return(s)

size = int(input())
edges = eval(input())
WL = {}
for i in range(size):
    WL[i] = []
for ed in edges:
    WL[ed[0]].append((ed[1],ed[2]))
    WL[ed[1]].append((ed[0],ed[2]))
print(FiberLink(WL))