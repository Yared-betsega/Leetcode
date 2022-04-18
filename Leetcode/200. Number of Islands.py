# https://leetcode.com/problems/number-of-islands/

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        # Union find solution
        def find_set(i):
            if i == parent[i]:
                return i
            parent[i] = find_set(parent[i])
            return parent[i]
        
        def union_sets(i, j):
            a = find_set(i)
            b = find_set(j)
            if a!=b:
                if size[a] >= size[b]:
                    parent[b] = a
                    size[a] += size[b]
                else:
                    parent[a] = b
                    size[b] += size[a]
                    
        parent, size = {}, {}
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    cur = (i, j)
                    parent[cur] = cur
                    size[cur] = 1
                    
                    if j - 1 >= 0 and grid[i][j-1] == "1":
                        union_sets(cur, (i, j-1))
                    if i - 1 >= 0 and grid[i-1][j] == "1":
                        union_sets(cur, (i-1, j))
        ans = 0
        for i in parent.keys():
            if find_set(i) == i:
                ans += 1
        return ans
                        
        
        
        
