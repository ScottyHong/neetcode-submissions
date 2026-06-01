class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        #Initialize pointer
        l,r = 1, 1
        while r < len(nums):
            #Case where we encounter something unique
            if nums[r] != nums[r-1]:
                nums[l] = nums[r]
                l += 1
            r += 1

        return l
