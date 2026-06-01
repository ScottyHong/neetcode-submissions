class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        new_nums = nums.copy()
        final = nums + new_nums
        return final