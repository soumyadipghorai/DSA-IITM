def LDS(L):
    if not L:
        return
    LDS = [[] for _ in range(len(L))]
    LDS[0].append(L[0])
    for i in range(1, len(L)):
        for j in range(i):
            if L[j] > L[i] and len(LDS[j]) > len(LDS[i]):
                LDS[i] = LDS[j].copy()
        LDS[i].append(L[i])
    j = 0
    for i in range(len(L)):
        if len(LDS[j]) < len(LDS[i]):
            j = i

    return LDS[j]

