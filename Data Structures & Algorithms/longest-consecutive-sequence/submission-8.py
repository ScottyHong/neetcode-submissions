class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        start_hash = {}
        numbers_set = set(nums)

        for num in nums:
            if (num-1) not in numbers_set:
                start_hash[num] = [num]
                i = 1
                while (num+i) in numbers_set:
                    start_hash[num].append(num+i)
                    i += 1
        
        length = 0
        for key in start_hash.keys():
            length = max(length, len(start_hash[key]))
        return length
                


