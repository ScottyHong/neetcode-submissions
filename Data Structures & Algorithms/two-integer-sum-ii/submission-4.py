class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        L, R = 0, (len(numbers)-1)
        adding = numbers[L] + numbers[R]

        while L < R:
            adding = numbers[L] + numbers[R]
            if adding > target:
                R -= 1
            elif adding < target:
                L += 1
            else:
                return [L+1,R+1]

        return []
            