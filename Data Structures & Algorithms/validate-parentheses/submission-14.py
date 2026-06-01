class Solution:
    def isValid(self, s: str) -> bool:
        #We can create a hash map
        #Create a stack to use
        close_to_open = {"}":"{", "]":"[", ")":"("}
        valid_open = "{(["
        stack = []
        for char in s:
            if char in valid_open:
                stack.append(char)
            elif char in close_to_open:
                if stack and close_to_open[char] == stack[-1]:
                    stack.pop()
                else:
                    return False

        if not stack:
            return True
        else:
            return False