class NumberContainers:

    def __init__(self):
        self.container = defaultdict(int)
        self.indices = defaultdict(list)
        self.removed = defaultdict(set)
    def change(self, index: int, number: int) -> None:
        if self.container[index] != 0:
            self.removed[self.container[index]].add(index)
        self.container[index] = number
        heappush(self.indices[number], index)
        if index in self.removed[number]:
            self.removed[number].remove(index)
    def find(self, number: int) -> int:
        if not self.indices[number]:
            return -1
        while self.indices[number] and self.indices[number][0] in self.removed[number]:
            heappop(self.indices[number])
        
        return self.indices[number][0] if self.indices[number] else -1

# Your NumberContainers object will be instantiated and called as such:
# obj = NumberContainers()
# obj.change(index,number)
# param_2 = obj.find(number)