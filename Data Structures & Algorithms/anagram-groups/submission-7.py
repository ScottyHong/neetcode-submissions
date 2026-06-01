class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #key, count value, list with words
        freq_dic = {}
        anagrams = []
        for word in strs:
            freq = [0]*26
            for char in word:
                count = (ord(char)-ord("a"))
                freq[count] += 1
            tup_freq = tuple(freq)
            if tup_freq not in freq_dic:
                freq_dic[tup_freq] = [word]
            else:
                freq_dic[tup_freq].append(word)
        for lst in freq_dic.values():
            anagrams.append(lst)
        return anagrams