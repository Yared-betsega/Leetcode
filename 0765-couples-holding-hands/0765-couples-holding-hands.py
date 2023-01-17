class Solution:
    def minSwapsCouples(self, row: List[int]) -> int:
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
                return 1
            return 0
        
        ans = 0
        parent = defaultdict(int)
        size = defaultdict(lambda: 1)
        for i in range(0, len(row) - 1, 2):
            x, y = row[i], row[i + 1]
            parent[x] = x
            parent[y] = x
            
        ans = 0
        for i in range(0, len(row) - 1, 2):
            x, y = i, i + 1
            ans += merge(x, y)
        return ans