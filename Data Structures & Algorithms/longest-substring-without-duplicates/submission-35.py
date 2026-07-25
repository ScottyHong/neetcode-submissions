class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        visited = set()

        l,r = 0, 0
        length = 0

        while r < len(s):
            print(visited)
            if s[r] in visited:
                visited.remove(s[l])
                l += 1
            elif s[r] not in visited:
                visited.add(s[r])
                curr_length = r-l + 1
                length = max(curr_length, length)
                r += 1
        
        return length


