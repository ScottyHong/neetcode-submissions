class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """
        A function that takes a unique list of ascending integers 
        and returns its index using a target, otherwise returns -1
        Parameters: List of distinct and ascending integers, target
        Returns: Index or -1
        """
        #We can use the binary search
        #Set Pointers that point to the ends of the search range
        #We can add the pointers together and see if there is a target
        #If not, we can eliminate half of the array

        Left, Right = 0, len(nums)-1
        Mid = (Left+Right)//2

        while Left <= Right:
            Mid = (Left+Right)//2
            if nums[Mid] < target:
                Left = Mid + 1
            elif nums[Mid] > target:
                Right = Mid - 1
            else:
                return Mid

        return -1