class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        def find(x):
            if parent[x] == x:
                return x
            parent[x] = find(parent[x])
            return parent[x]
        
        def merge(x, y):
            a = find(x)
            b = find(y)
            
            if a != b:
                if size[b] > size[a]:
                    a, b = b, a
                
                parent[b] = a
                size[a] += size[b]
                size[b] = 0
                
        ans = None
        parent = defaultdict(int)
        size = defaultdict(lambda: 1)
        for i, (x, y) in enumerate(edges):
            if parent[x] == 0:
                parent[x] = x
            if parent[y] == 0:
                parent[y] = y
            if find(x) != find(y):
                merge(x, y)
            else:
                ans = [x, y]
        
        return ans