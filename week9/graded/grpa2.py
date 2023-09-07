memo = None
def MaxCoinPath(M, x1, y1, x2, y2):
    global memo
    if memo is None:
        memo = [[0 for i in range(len(M[0]))] for j in range(len(M))]
    if x2 == x1 and y2 == y1:
        return M[x1][y1]
    if x2 < 0 or y2 < 0:
        return 0
    #print(x2,y2)
    mx = max(MaxCoinPath(M, x1, y1, x2 - 1, y2), MaxCoinPath(M, x1, y1, x2, y2 - 1))
    #print("mx:",mx)
    memo[x2][y2] = mx+M[x2][y2] if mx > memo[x2][y2] else memo[x2][y2]

    return memo[x2][y2]

M = eval(input())
(x1,y1)=eval(input())
(x2,y2) = eval(input())
print(MaxCoinPath(M,x1,y1,x2,y2))