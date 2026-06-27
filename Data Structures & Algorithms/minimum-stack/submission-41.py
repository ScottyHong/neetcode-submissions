class MinStack:

    def __init__(self):
        self.stack = []
        self.min_stack = [] #This will act like a prefix minimum
        self.min_val = float('inf')

    def push(self, val: int) -> None:
        self.min_val = min(self.min_val, val)
        self.stack.append(val)
        self.min_stack.append(self.min_val)

    def pop(self) -> None:
        self.stack.pop()
        self.min_stack.pop()
        self.min_val = self.min_stack[-1] if self.min_stack else float('inf')


    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]
