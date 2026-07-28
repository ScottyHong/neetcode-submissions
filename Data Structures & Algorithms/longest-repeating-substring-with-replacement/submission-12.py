class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        L,R = 0,0
        maxFreq = 0
        result = 0
        count = {}

        while R < len(s):
            window_length = R - L + 1
            char = s[R]
            
            if char in count:
                count[char] += 1
            else:
                count[char] = 1

            maxFreq = max(maxFreq, count[char])
            #We need to check if the condition is true
            print(window_length)
            print(maxFreq)
            if window_length - maxFreq <= k:
                result = max(window_length, result)
                print(f'condition holds: {result}')
            else:
                count[s[L]] -= 1
                L += 1
            R += 1
        return result
