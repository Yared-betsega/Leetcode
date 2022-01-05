class MyQueue:

    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def push(self, x: int) -> None:
        self.stack1.append(x)

    def pop(self) -> int:
        while len(self.stack1) > 0:
            self.stack2.append(self.stack1.pop())
        popped = self.stack2.pop()
        while len(self.stack2) > 0:
            self.stack1.append(self.stack2.pop())
        return popped
    def peek(self) -> int:
        while len(self.stack1) > 0:
            self.stack2.append(self.stack1.pop())
        peeked = self.stack2[-1]
        while len(self.stack2) > 0:
            self.stack1.append(self.stack2.pop())
        return peeked

    def empty(self) -> bool:
        if len(self.stack1) == 0:
            return True
        else:
            return False
