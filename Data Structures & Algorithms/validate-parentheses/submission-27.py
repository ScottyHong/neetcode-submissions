class Solution:
    def isValid(self, s: str) -> bool:
        close_to_open = {"}":"{","]":"[",")":"("}
        stack = []

        for char in s:
            if char not in close_to_open:
                #If this is an opening bracket, put it in stack
                stack.append(char)
            elif char in close_to_open:
                if stack and stack[-1] == close_to_open[char]:
                    stack.pop()
                else:
                    return False
        
        if stack:
            return False
        else:
            return True


