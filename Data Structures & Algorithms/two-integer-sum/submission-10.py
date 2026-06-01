class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #Hashing something
        #Maybe we can create a dictionary that like has the solution as the key
        #Let's create a hash map that maps 
        #value to index
        solutions = {}
        for ind, num in enumerate(nums):
            difference = target - num
            if difference not in solutions:
                solutions[num] = ind
            else: 
                ind_lst = sorted([solutions[difference], ind])
                return ind_lst
        
