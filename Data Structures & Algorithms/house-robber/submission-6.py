class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = {}
        def dp(nums):
            if len(nums) == 0:
                return 0
            if len(nums) == 1:
                return nums[0]
            if len(nums) in memo:
                return memo[len(nums)]

            skipped = dp(nums[1:])
            robbed = dp(nums[2:]) + nums[0]

            value = max(skipped,robbed)

            memo[len(nums)] = value
            return value
        return dp(nums)
        