def maxProfit(array):
    profit = 0
    buy = array[0] 
    min = buy
    for i in range(1, len(array)):
        if array[i] < min:
            min = array[i]
        else:
            if profit < array[i] - min:
                profit = array[i] - min
                sell = array[i]
                buy = min
                

    return [buy, sell]

def maxSingleSellProfit(a):
    buy = a[0]
    min = buy
    profit = 0
    for i in range(1, len(a)):
        if a[i] > min:
            if profit < a[i] - min:
                profit = a[i] - min
        if a[i] < min:
            min = a[i]
    return profit

a = [5, 7, 2, 4, 3, 50]
print(maxProfit(a))
print(maxSingleSellProfit(a))
prices = [7,1,5,3,6,4]
print(maxProfit(prices))
print(maxSingleSellProfit(prices))
prices = [7,2,5,3,6,4,1]
print(maxProfit(prices))
print(maxSingleSellProfit(prices))