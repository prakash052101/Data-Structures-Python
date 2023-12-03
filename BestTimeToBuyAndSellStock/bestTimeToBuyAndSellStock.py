#Best Time to Buy and Sell Stock
#time complexity - O(n), where n is the number of elements in the prices array

def maxProfit(prices) -> int:
    Profit = 0
    buy = prices[0]
    for price in prices:
        if price < buy:
            buy = price
            
        elif (price - buy) > Profit:
            Profit = price - buy

    return Profit

if __name__ == "__main__":
    prices = [7,1,5,3,6,4]
    print(maxProfit(prices))