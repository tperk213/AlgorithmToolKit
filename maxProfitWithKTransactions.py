
#Time (k*N^2)
#Space (kN + N)
# def maxProfitWithKTransactions(array, k):
#     if len(array) < 2:
#         return 0
#     profit = [[0 for i in range(len(array))] for j in range(k+1)]

#     for i in range(1, k+1):
#         for j in range(1, len(array)):
#             profitsWith1LessTransaction = []
#             for k in range(0,j):
#                 if k >= 1:
#                     profitsWith1LessTransaction.append(-array[k]+profit[i-1][k-1])
#                 else:
#                     profitsWith1LessTransaction.append(-array[k])
#             profit[i][j] = max(profit[i][j-1], array[j] + max(profitsWith1LessTransaction))
    
#     return profit[-1][-1]

def maxProfitWithKTransactions(array, k):
    oddProfit = [0 for i in range(len(array))]
    evenProfit = [0 for i in range(len(array))]
    for i in range(1, k+1):
        maxThusFar = float("-inf")
        if i % 2 == 0:
            currentProfits = evenProfit
            previousProfit = oddProfit
        else:
            currentProfits = oddProfit
            previousProfit = evenProfit
        for j in range(1, len(array)):
            maxThusFar = max(maxThusFar, previousProfit[j-1] - array[j-1])
            currentProfits[j] = max(currentProfits[j-1], maxThusFar + array[j])

    return evenProfit[-1] if k%2 == 0 else oddProfit[-1]


if __name__ == "__main__":
    prices = [5,11,3,50,60,90]
    k = 2
    z = maxProfitWithKTransactions(prices, k)
    print(z)
# #transaction is buy and sell

# prices = [5,11,3,50,60,90] k=2
# #use dynamic programming

# #   5   11  3   50  60  90
# #0  0   0   0   0   0   0
# #1  0   6   6   47  57  87   
# #2  0   6   6   53  63  93

#Max thus far
# maxThusFar = max(maxThusFar, previousProfits[j-1]-prices[j-1], )
#           -5  -5  -3  -3  -3
#               -5  -3  -3
# profit[t][d] = max(
#                     profit[t][d-1],
#                     for x in range(d):
#                         prices[d] - princes[x] + profit[t-1][x]
#                     )