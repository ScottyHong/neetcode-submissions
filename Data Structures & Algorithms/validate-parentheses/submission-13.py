class Solution:
    def isValid(self, s: str) -> bool:
        #We can use recursion and a hash map
        close_to_open = {"]":"[", "}":"{", ")":"("}
        stack = []
        
        for char in s:
            if char in close_to_open:
                if stack and stack[-1] == close_to_open[char]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)
        
        if not stack:
            return True
        else:
            return False