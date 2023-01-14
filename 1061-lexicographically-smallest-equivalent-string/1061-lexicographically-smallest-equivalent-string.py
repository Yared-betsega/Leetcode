class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        parent = defaultdict(int)
        
        def find(x):
            if x == parent[x]:
                return x
            parent[x] = find(parent[x])
            return parent[x]
        
        def union(x, y):
            a = find(x)
            b = find(y)
            if ord(a) <= ord(b):
                parent[b] = a
            else:
                parent[a] = b
        
        for i in range(len(s1)):
            if parent[s1[i]] == 0:
                parent[s1[i]] = s1[i]
            if parent[s2[i]] == 0:
                parent[s2[i]] = s2[i]
            union(s1[i], s2[i])
        
        ans = []
        for char in baseStr:
            par = find(char)
            if par != 0:
                ans.append(par)
            else:
                ans.append(char)
        return "".join(ans)