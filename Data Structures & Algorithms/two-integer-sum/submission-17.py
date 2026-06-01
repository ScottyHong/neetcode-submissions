class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        target_hash = {}
        for ind, num in enumerate(nums):
            val = target - num
            if val not in target_hash:
                target_hash[num] = ind
            else:
                return [target_hash[val], ind]