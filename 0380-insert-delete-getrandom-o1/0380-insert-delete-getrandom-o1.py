class RandomizedSet:

    def __init__(self):
        self.index = {}
        self.list = []
        
    def insert(self, val: int) -> bool:
        if val in self.index:
            return False
        self.index[val] = len(self.list)
        self.list.append(val)
        return True
    
    def remove(self, val: int) -> bool:
        if val not in self.index:
            return False
        ind = self.index[val]
        self.index[self.list[-1]] = ind
        del self.index[val]
        self.list[ind], self.list[-1] = self.list[-1], self.list[ind]
        self.list.pop()
        return True
    
    def getRandom(self) -> int:
        return self.list[random.randint(0, len(self.list) - 1)]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()