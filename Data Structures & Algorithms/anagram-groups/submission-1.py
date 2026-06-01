class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #Hash the frequency to the list of words
        final_dict = defaultdict(list)

        for word in strs:
            count = [0] * 26
            for char in word:
                count[ord(char)-ord("a")] +=1
            final_dict[tuple(count)].append(word)
          
        return list(final_dict.values())