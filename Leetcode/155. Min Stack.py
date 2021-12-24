class MinStack:

    def __init__(self):
        self.lst = []
        
    def push(self, val: int) -> None:
        self.lst.append(val)
        self.min = min(self.lst)
        
    def pop(self) -> None:
        self.lst.pop()
        if len(self.lst)>0:
            self.min = min(self.lst)
    def top(self) -> int:
        return self.lst[-1]

    def getMin(self) -> int:
        return self.min
