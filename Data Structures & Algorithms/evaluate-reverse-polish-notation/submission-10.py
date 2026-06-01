class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        #Let us use recursion
        valid = "+*/-"
        def recursion():
            token = tokens.pop()
            if token not in valid:
                return int(token)
            right = recursion()
            left = recursion()
         
            if token == "+":
                return left + right
            elif token == "-":
                return left - right
            elif token == "*":
                return left * right
            elif token == "/":
                return int(left/right)
        
        return recursion()