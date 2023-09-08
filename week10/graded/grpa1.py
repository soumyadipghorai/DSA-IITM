def findContinuousRepetitions(t, p):
    last = {}
    for i in range(len(p)):
        last[p[i]] = i
        
    goldFlag = False
    goldCount = 0
    goldtemp = 0
        
    poslist, i = [], 0
    while i <= (len(t) - len(p)):
        matched, j = True, len(p)-1
        while j >= 0 and matched:
            if t[i+j] != p[j]:
                matched = False
            j -= 1
        if matched:
            
            goldFlag = True
            poslist.append(i)
            if goldFlag:
                goldtemp += 1
                if goldtemp>goldCount:
                    goldCount = goldtemp
            i += len(p)
        else:
            goldFlag = False
            goldtemp = 0
            j += 1
            if t[i+j] in last.keys():
                i += max(j-last[t[i+j]], 1)
            else:
                i += j + 1
    return(goldCount)

t = input()
p = input()
print(findContinuousRepetitions(t, p))