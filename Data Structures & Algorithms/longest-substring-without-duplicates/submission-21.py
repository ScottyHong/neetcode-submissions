class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hash_map = {}
        L = 0
        length = 0

        for R in range(len(s)):
            if s[R] in hash_map:
                L = max(hash_map[s[R]]+1,L)
            hash_map[s[R]] = R
            length = max(length, R-L+1)

        return length