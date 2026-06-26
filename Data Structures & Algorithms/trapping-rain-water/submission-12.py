class Solution:
    def trap(self, height: List[int]) -> int:
        L, R = 0, (len(height)-1)
        total_area = 0
        max_left = height[L]
        max_right = height[R]

        while L < R:
            if max_left < max_right:
                L += 1
                max_left = max(max_left, height[L])
                total_area += max_left - height[L]
            else:
                R -= 1
                max_right = max(max_right, height[R])
                total_area += max_right - height[R]

        return total_area