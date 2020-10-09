def minNumofCoinsForChange(n, denoms):
    numOfCoins = [float("inf") for amount in range(n+1)]
    numOfCoins[0] = 0
    for denom in denoms:
        for amount in range(len(numOfCoins)):
            if denom <= amount:
                numOfCoins[amount] = min(
                    numOfCoins[amount], 1 + numOfCoins[amount-denom])
    print(numOfCoins)
    return numOfCoins[n] if numOfCoins[n] != float('inf') else -1


print(minNumofCoinsForChange(11, [5, 4, 2]))
print(minNumofCoinsForChange(7, [2, 4]))
