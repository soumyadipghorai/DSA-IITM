def stringmatch(t, p):
    poslist = []
    for i in range(len(t) - len(p) + 1):
        matched = True
        j = 0
        while j < len(p) and matched:
            if t[i+j] != p[j] and p[j] != "$":
                matched = False
            j += 1
        if matched:
            poslist.append((i, t[i:i+len(p)]))
    return(poslist)
    
def stringmatchrev(t, p):
    poslist = []
    for i in range(len(t) - len(p) + 1):
        matched = True
        j = len(p) - 1
        while j >= 0 and matched:
            if t[i+j] != p[j] and p[j] != "$":
                matched = False
            j -= 1
        if matched:
            poslist.append((i, t[i:i+len(p)]))
    return(poslist)
    
def FindPattern(t,p):
    if p[0] == "$":
        return stringmatch(t, p)
    else:
        return stringmatchrev(t, p)

T = input()
P = input()
print(FindPattern(T,P))