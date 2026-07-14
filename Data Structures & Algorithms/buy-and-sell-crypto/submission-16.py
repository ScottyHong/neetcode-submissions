class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l,r = 0,1
        biggest = 0
        
        while r <= len(prices)-1:
            curr_ele = prices[r] - prices[l]
            if curr_ele < 0:
                l = r
            else:
                biggest = max(curr_ele, biggest)
            r+= 1
        
        return biggest


