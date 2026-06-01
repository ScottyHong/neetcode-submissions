class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #Let's set left and right pointers
        #We can subtract pointer positions, if it's negative, 
        #We can move the left and right pointer together, otherwise just the right pointer moves

        left, right = 0, 1
        maxP = 0
        while right < len(prices):
            if (prices[right] - prices[left]) < 0:
                left = right
            elif (prices[right] - prices[left]) > 0:
                profit = (prices[right]-prices[left])
                maxP = max(maxP, profit)
            right += 1
        
        return maxP

            