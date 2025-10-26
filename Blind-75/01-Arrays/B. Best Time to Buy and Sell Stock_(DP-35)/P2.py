# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/
# Best Time to Buy and Sell Stock

from typing import List

def maxProfit_bruteForce(prices: List[int]) -> int:
    maxProfit = 0
    for firstTransact in range(len(prices)):
        for secondTransaction in range(firstTransact+1, len(prices)):
            currentProfit = prices[secondTransaction]-prices[firstTransact]
            if currentProfit > maxProfit:
                maxProfit = currentProfit

    return 0 if maxProfit<=0 else maxProfit


def maxProfit_optimized(prices: List[int]) -> int:
    min_price = float('inf')
    max_profit = 0
    for price in prices:
        if price < min_price:
            min_price = price
        elif price - min_price > max_profit:
            max_profit = price - min_price
    return max_profit


if __name__=="__main__":
    # INPUT
    prices1 = [7,1,5,3,6,4] # 5
    prices2 = [7,6,4,3,1] # 0

    print(maxProfit_optimized(prices1))
    
