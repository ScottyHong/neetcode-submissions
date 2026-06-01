class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #Hashing of some sort
        #Maybe we can put together 
        final_dict = defaultdict(list)
       
        for word in strs:
            count = [0] * 26
            for char in word:
                count[ord(char) - ord("a")] += 1
            final_dict[tuple(count)].append(word)
      
        return list(final_dict.values())
