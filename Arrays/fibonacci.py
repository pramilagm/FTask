def fibonacciNum(k):
    if k <= 1:
        return k
    return fibonacciNum(k-1) + fibonacciNum(k-2)


print(fibonacciNum(4))
