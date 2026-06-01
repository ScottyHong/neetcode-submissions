class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        L, R = 0,1
        max_profit = 0
        curr_profit = 0

        while R < len(prices):
            if prices[L] > prices[R]:
                L = R
                R += 1
            elif prices[L] <= prices[R]:
                curr_profit = prices[R] - prices[L]
                max_profit = max(curr_profit, max_profit)
                R+=1
            

        return max_profit
