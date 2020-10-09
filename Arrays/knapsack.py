def knapSack(W, wt, values, n):
    K = [[0 for i in range(W+1)] for j in range(n+1)]
    for i in range(n+1):
        for w in range(W+1):
            if i == 0 or w == 0:
                K[i][w] = 0
            elif wt[i-1] <= w:
                K[i][w] = max(K[i-1][w], val[i-1] + K[i-1][w-wt[i-1]])
            else:
                K[i][w] = K[i-1][w]
    return K[n][W]


val = [50, 100, 150, 200]
wt = [8, 16, 32, 40]
W = 64
n = len(val)
print(knapSack(W, wt, val, n))
