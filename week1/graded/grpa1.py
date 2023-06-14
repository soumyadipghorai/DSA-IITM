def find_Min_Difference(L, P) : 
    L.sort()
    subset = L[:P]
    min_diff = max(L) 
    for i in range(len(L)-P+1) : 
        subset = L[i:i+P]
        if max(subset) - min(subset) < min_diff : 
            min_diff = max(subset) - min(subset)
    
    return min_diff

L=eval(input().strip())
P=int(input())
print(find_Min_Difference(L,P))