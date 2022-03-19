
# https://leetcode.com/problems/maximum-frequency-stack/

import heapq as hq
class FreqStack:

    def __init__(self):
        self.freqStack = []
        self.freq = defaultdict(int)
        self.prec = 0
        

    def push(self, val: int) -> None:
        self.freq[val] += 1
        self.prec += 1
        hq.heappush(self.freqStack, [-1*self.freq[val], -1*self.prec, val])
        
    def pop(self) -> int:
        val = hq.heappop(self.freqStack)[2]
        self.freq[val] -= 1
        return val
        
# time and space complexity 
# time comolexity = O(log(n)) for both push and pop function
# n == len(freqStack) at any moment
# space complexity = O(n)
