""" You are given an integer array prices where prices[i] is the price of a given stock on the ith day.

On each day, you may decide to buy and/or sell the stock. You can only hold at most one share of the stock at any time. 

However, you can buy it then immediately sell it on the same day.

Find and return the maximum profit you can achieve. """

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1
        profits = []
        total = 0
        
        # loop while r < prices
        while r < len(prices):
            # calc profit if l < r
            # add profit to array and increment l pointer
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                profits.append(profit)
                l += 1
            # else r is less than l, so we want l to equal r
            else:
                l = r
            # continue to increment r pointer
            r += 1
        
        # loop profits array and sum the total
        for num in profits:
            total += num
            
        return total