class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #Loop through the strings
        #Initialize a Hash Map where we have frequencies and lists that match the frequency
        grp_ana = []
        group_freq = {}
        for word in strs:
            freq = {}
            for char in word:
                if char not in freq:
                    freq[char] = 1
                else:
                    freq[char] += 1
            key = frozenset(freq.items())
            if key not in group_freq:
                group_freq[key] = [word]
            else: 
                group_freq[key].append(word)

        for key, value in group_freq.items():
            grp_ana.append(value)

        return grp_ana


        