class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        frequencies = [[] for i in range(len(nums) + 1)]
        for num in nums:
            if num in count:
                count[num] += 1
            else:
                count[num] = 1

        for key,val in count.items():
            frequencies[val].append(key)

        res = []
        for ind in range(len(frequencies)-1,0,-1):
            for num in frequencies[ind]:
                res.append(num)
                if len(res) ==k:
                    return res