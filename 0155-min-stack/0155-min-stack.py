class MinStack:

    def __init__(self):
        self.stack = []
        self._min = float("inf")
        
    def push(self, val: int) -> None:
        self.stack.append((val, self._min))
        self._min = min(self._min, val)

    def pop(self) -> None:
        self._min = self.stack.pop()[1]

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self._min


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()