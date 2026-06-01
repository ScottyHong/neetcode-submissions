class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        L,R = 1, max(piles)
        result = R

        while L <= R:
            k = (L+R)//2
            hours = 0
            for p in piles:
                hours += math.ceil(float(p)/k)

            if hours <= h:
                result = k
                R = k-1

            elif hours > h:
                L = k+1

        return result