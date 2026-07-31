class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""
        
        res = ""
        L, R = 0, 0 

        freq_t = [0] * 100
        freq_res = [0] * 100
        
        for char in t:
            index = ord(char) - ord('A')
            freq_t[index] += 1
        
        def is_satisfied():
            for i in range(100):
                if freq_res[i] < freq_t[i]:
                    return False
            return True

        while R < len(s) or is_satisfied():
            if is_satisfied():
                curr_sub = s[L:R]
                if res == "" or len(curr_sub) < len(res):
                    res = curr_sub
                index = ord(s[L]) - ord('A')
                freq_res[index] -= 1
                L += 1
            else:
                index = ord(s[R]) - ord('A')
                freq_res[index] += 1
                R += 1

        return res