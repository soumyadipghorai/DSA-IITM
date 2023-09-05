def no_overlap(L):
    L_sort = sorted(L,key=lambda s:(s[2],s[1]))
    accepted = []
    end_day = 0
    for k in L_sort:
        if k[1] > end_day:
            end_day = k[2]
            accepted.append(k)
    return (accepted)
        
       