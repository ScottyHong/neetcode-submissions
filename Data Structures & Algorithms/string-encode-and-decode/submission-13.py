class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_str = ""
        sizes = []
        for string in strs:
            size_of_string = len(string)
            encoded_str += str(size_of_string)
            encoded_str += "#"
            encoded_str += string
        print(encoded_str)
        return encoded_str

    def decode(self, s: str) -> List[str]:
        decoded_list = []
        i = 0

        while i < len(s):
            j = i
            while s[j] != "#":
                j+=1
            length = int(s[i:j])
            i = j+1
            j = i+length
            decoded_list.append(s[i:j])
            i = j
                
        return decoded_list