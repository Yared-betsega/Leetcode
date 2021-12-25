class MyCircularDeque:

    def __init__(self, k: int):
        self.deque = []
        self.size = k
    def insertFront(self, value: int) -> bool:
        if len(self.deque) < self.size:
            self.deque.insert(0, value)
            return True
        else:
            return False

    def insertLast(self, value: int) -> bool:
        if len(self.deque) < self.size:
            self.deque.append(value)
            return True
        else:
            return False

    def deleteFront(self) -> bool:
        if len(self.deque) > 0:
            self.deque.pop(0)
            return True
        else:
            return False

    def deleteLast(self) -> bool:
        if len(self.deque) > 0:
            self.deque.pop()
            return True
        else:
            return False

    def getFront(self) -> int:
        if len(self.deque) > 0:
            return self.deque[0]
        else:
            return -1

    def getRear(self) -> int:
        if len(self.deque) > 0:
            return self.deque[-1]
        else:
            return -1
    def isEmpty(self) -> bool:
        if len(self.deque) == 0:
            return True
        else:
            return False

    def isFull(self) -> bool:
        if len(self.deque) == self.size:
            return True
        else:
            return False
