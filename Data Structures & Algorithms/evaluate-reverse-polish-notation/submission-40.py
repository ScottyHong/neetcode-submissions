class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = {'+','-','*','/'}
        total_value = 0
        while tokens:
            token = tokens.pop(0)
            if token not in operators:
                stack.append(token)
            else:
                #print(token)
                if stack:
                    val_1 = int(stack.pop())
                    val_2 = int(stack.pop())
                    curr_val = 0
                    if token == '+':
                        curr_val = val_2 + val_1
                        total_value = curr_val
                        stack.append(total_value)
                        #print(f"after append {stack}")
                    elif token == '-':
                        curr_val = val_2 - val_1
                        total_value = curr_val
                        print(total_value)
                        stack.append(total_value)
                        print(stack)
                    elif token == '*':
                        curr_val = val_2 * val_1
                        total_value = curr_val
                        stack.append(total_value)
                    elif token == '/':
                        curr_val = val_2 / val_1
                        total_value = curr_val
                        stack.append(total_value)

        return int(stack[-1])