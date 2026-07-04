import math 

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        best = r
        while l <= r:
            time = 0
            eating_rate = l + (r-l)//2

            for pile in piles:
                time += math.ceil(pile/eating_rate)
            if time > h:
                l = eating_rate + 1
            else:
                best = eating_rate
                r = eating_rate - 1

        return best
