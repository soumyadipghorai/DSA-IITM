def maxLessThan(root, K):
    max = root.value
    temp = root
    while (not temp.isempty()):
        if (temp.value and K<temp.value):
            temp = temp.left
        elif (temp.value and K>=temp.value):
            max = temp.value
            temp = temp.right
    if (K >= max):
        return max
    else:
        return None

k = int(input())
LL=[]
for i in range(k):
    subL = [int(item) for item in input().split(" ")]
    LL.append(subL)
print(*mergeKLists(LL))