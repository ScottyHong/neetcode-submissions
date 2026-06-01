class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        target_hash = {}
        for i, num in enumerate(nums):
            hash_func = target-num
            print(hash_func)
            if num not in target_hash:
                target_hash[hash_func] = i
            elif num in target_hash:
                return [target_hash[num], i]