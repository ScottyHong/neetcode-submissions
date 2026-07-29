class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        L, R = 0, len(s1)-1
        
        freq_s1 = [0] * 26
        result = [0] * 26

        for ind in range(len(s1)):
            ind1 = ord(s1[ind]) - ord('a')
            ind2 = ord(s2[ind])- ord('a')
            freq_s1[ind1] += 1
            result[ind2] += 1

        while R < len(s2) -1:
            if freq_s1 == result:
                return True
            else:
                #We need to decrement the left pointer element
                left_ind = ord(s2[L]) - ord('a')
                result[left_ind] -= 1

                L += 1
                R += 1
                right_ind = ord(s2[R]) - ord('a')
                result[right_ind] += 1


        return freq_s1 == result
