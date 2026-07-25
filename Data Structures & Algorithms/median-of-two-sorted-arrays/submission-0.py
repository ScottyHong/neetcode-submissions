class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2
        #We need to get the total and the half to take advantage
        #of the sorted arrays

        total = len(nums1) + len(nums2)
        half = total // 2
        
        if len(B) < len(A):
            A, B = nums2, nums1

        L, R = 0, len(A)-1
        #We should do binary search onto the smaller array
        #If there are evens, odds
        #We are trying to see of the ost right on the left is smaller than
        #The most left on the right
        while True:
            i = (L+R)//2 
            j = half - i -2
            #Define border values
            if i >= 0:
                Aleft = A[i]
            else: 
                Aleft = -float('inf')
            if i +1 < len(A):
                Aright = A[i+1]
            else:
                Aright = float('inf')
            if j >= 0:
                Bleft = B[j]
            else:
                Bleft = -float('inf')
            if j + 1 < len(B):
                Bright = B[j+1]
            else:
                Bright = float('inf')

        
            if Aleft <= Bright and Bleft <= Aright: #Correct partition
                if total % 2 != 0:
                    return min(Aright,Bright)
                else:
                    return (max(Aleft,Bleft) + min(Aright, Bright)) /2
            elif Aleft > Bright:
                R = i - 1
            else:
                L = i + 1

                
