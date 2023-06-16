def combinationSort(L) : 
    str_split = [(val[0], int(val[1:])) for val in L]
    L2_copy = sorted(str_split, key = lambda x : (x[0], -x[1]))
    L1_copy = sorted(str_split, key = lambda x: x[0])
    L2 = [val[0]+str(val[1]) for val in L2_copy]
    L1 = [val[0]+str(val[1]) for val in L1_copy]
    
    return L1, L2