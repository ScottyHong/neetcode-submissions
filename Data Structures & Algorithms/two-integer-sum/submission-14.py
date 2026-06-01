class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # declare a hash map {} to store index i and value = target - nums[i]

        difference = dict()

        for i in range(len(nums)):
            if nums[i] in difference.keys():
                return [difference[nums[i]], i]

            else:
                difference[target - nums[i]] = i



        # difference = dict()

        # #iterate through the array – index specific
        # for i in range(len(nums)):
	    #     #check if exists as value in hash map
        #     if nums[i] in difference.keys():
		#     #if yes – return i, j
		#         return difference[nums[i]], i
		
		#     #else - append the difference and index
        #     else:	
		#         difference[target - nums[i]] = i

