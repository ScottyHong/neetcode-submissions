class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for ind,number in enumerate(nums):
            difference = target - number
            if difference not in hashmap:
                hashmap[number] = ind
            elif difference in hashmap:
                return [hashmap[difference], ind]