class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_set = set(s)
        t_set = set(t)
        if len(s) != len(t):
            return False
        if len(s_set) != len(t_set):
            return False
        elif len(s_set) == len(t_set):
            if sorted(s) == sorted(t):
                return True
            else:
                return False