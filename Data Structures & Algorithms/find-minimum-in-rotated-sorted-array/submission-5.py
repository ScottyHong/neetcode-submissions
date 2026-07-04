class Solution:
    def findMin(self, nums: List[int]) -> int:
        flag = True
        l, r = 0, len(nums)-1
        best = nums[l]
        while True:
            if nums[l] > nums[r]:
                l = r 
            else:
                if l == 0:
                    return best
                if nums[l-1] > nums[l]:
                    best = nums[l]
                    break
                else:
                    l -= 1
        return best