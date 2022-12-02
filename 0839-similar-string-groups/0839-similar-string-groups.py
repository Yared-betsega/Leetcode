class UnionFind:
    def __init__(self):
        self.parent = {}
        self.size = defaultdict(int)
    
    def find(self, x):
        if x not in self.parent:
            return x
        
        if x == self.parent[x]:
            return x
        self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def merge(self, x, y):
        px = self.find(x)
        py = self.find(y)
        if px != py:
            if self.size[px] < self.size[py]:
                px, py = py, px
            self.parent[py] = px
            self.size[px] += self.size[py]
            
        
class Solution:
    def numSimilarGroups(self, strs: List[str]) -> int:
        pos = {}
        for i in range(len(strs)):
            pos[strs[i]] = i
            
        unionfind = UnionFind()
        for i in range(len(strs)):
            for j in range(i + 1, len(strs)):
                if self.check(strs[i], strs[j]):
                    unionfind.merge(pos[strs[i]], pos[strs[j]])
        
        groups = 0
        for st in pos:
            if pos[st] == unionfind.find(pos[st]):
                groups += 1
                
        return groups
    
    def check(self, s1, s2):
        diff = 0
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                diff += 1
        
        return diff == 2
    
                