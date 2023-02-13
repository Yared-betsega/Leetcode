class AllOne:
    def __init__(self):
        self.count = defaultdict(int)
        self.removed = defaultdict(int)
        self.minHeap = []
        self.maxHeap = []

    def inc(self, key: str) -> None:
        self.removed[(self.count[key], key)] += 1
        self.removed[(-self.count[key], key)] += 1
        self.count[key] += 1
        heapq.heappush(self.minHeap, (self.count[key], key))
        heapq.heappush(self.maxHeap, (-self.count[key], key))

    def dec(self, key: str) -> None:
        if self.count[key] > 0:
            self.removed[(self.count[key], key)] += 1
            self.removed[(-self.count[key], key)] += 1
            self.count[key] -= 1
            heapq.heappush(self.minHeap, (self.count[key], key))
            heapq.heappush(self.maxHeap, (-self.count[key], key))

    def getMaxKey(self) -> str:
        while len(self.maxHeap) > 0 and self.removed[self.maxHeap[0]] > 0:
            self.removed[self.maxHeap[0]] -= 1
            heapq.heappop(self.maxHeap)
        if len(self.maxHeap) > 0:
            return self.maxHeap[0][1]
        return ""

    def getMinKey(self) -> str:
        while len(self.minHeap) > 0 and self.removed[self.minHeap[0]] > 0:
            self.removed[self.minHeap[0]] -= 1
            heapq.heappop(self.minHeap)
        if len(self.minHeap) > 0:
            return self.minHeap[0][1]
        return ""