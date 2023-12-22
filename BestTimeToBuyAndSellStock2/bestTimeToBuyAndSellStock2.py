#Best Time to Buy and Sel Stock2
#time complexity - O(n)

def maxProfit(prices):
    profit = 0

    for i in range(1, len(prices)):
        if prices[i] > prices[i - 1]:
            profit += prices[i] - prices[i - 1]

    return profit

if __name__ == "__main__":
    prices1 = [7, 1, 5, 3, 6, 4]
    print(maxProfit(prices1))  

    prices2 = [1, 2, 3, 4, 5]
    print(maxProfit(prices2))  

    prices3 = [7, 6, 4, 3, 1]
    print(maxProfit(prices3)) 
