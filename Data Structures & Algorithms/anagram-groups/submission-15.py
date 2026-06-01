class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #Loop through the strings
        #Initialize a Hash Map where we have frequencies and lists that match the frequency
        anagram_hash = {}
        result = []
        for word in strs:
            frequency = [0] * 26
            for char in word:
                ind = ord(char) - 97
                frequency[ind] += 1
            new_freq = tuple(frequency)
            if new_freq not in anagram_hash:
                anagram_hash[new_freq] = [word]
            else:
                anagram_hash[new_freq].append(word)
        
        for words in anagram_hash.values():
            result.append(words)

        return result
        