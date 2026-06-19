class Solution:
    def isPalindrome(self, s: str) -> bool:
        L, R = 0, (len(s)-1)
        while L < R:
            print(s[L])
            print(s[R])
            while not s[L].isalnum() and L < R:
                L += 1
            while not s[R].isalnum() and R > L:
                R -= 1
            left = s[L].lower()
            right = s[R].lower()

            if left != right:
                return False
            L += 1
            R -= 1

        return True
                