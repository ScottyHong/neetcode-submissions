class Solution:
    def maxArea(self, heights: List[int]) -> int:
        L,R = 0,(len(heights)-1)
        max_area = 0
        for ind in range(len(heights)):
            width = (R-L)
            height = min(heights[L], heights[R])
            curr_area = width * height
            max_area = max(max_area, curr_area)

            if heights[L] < heights[R]:
                L += 1
            elif heights[L] > heights[R]:
                R -= 1
            else:
                R -= 1
        return max_area
