""" You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the

future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0. """

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # use a l and r pointer
        l,r = 0, 1
        max_profit = 0
        
        # loop while r < length of the list
        while r < len(prices):
            # if price at l is less than r, calc profit
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                max_profit = max(max_profit, profit)
            else:
                # shift l pointer to r, we want l to be the smallest number
                l = r
            
            # keep incrementing r pointer
            r += 1
        
        return max_profit