class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = []
        prefix = []
        postfix = []
        pre = 1
        post = 1
        for ind in range(len(nums)):
            prefix.append(pre)
            pre *= nums[ind]
        for ind in range(len(nums)-1, -1, -1):
            postfix.append(post)
            post *= nums[ind]

        postfix = postfix[::-1]
        for ind in range(len(nums)):
            result.append(prefix[ind] * postfix[ind])

        return result