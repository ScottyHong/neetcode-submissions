class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_hash = {}
        t_hash = {}
        if len(s) != len(t):
            return False
        else:
            for ind in range(len(s)):
                if s[ind] not in s_hash:
                    s_hash[s[ind]] = 1
                else:
                    s_hash[s[ind]] += 1
                if t[ind] not in t_hash:
                    t_hash[t[ind]] = 1
                else:
                    t_hash[t[ind]] += 1
        
            if s_hash != t_hash:
                return False
            else:
                return True