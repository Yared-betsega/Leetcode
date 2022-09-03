class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        ans = set()
        def dfs(b, path):
            path.append(b)
            if len(path) == n:
                ans.add(int("".join(map(str, path))))
            else:
                if b + k <= 9:
                    dfs(b + k, path)
                if b - k >= 0:
                    dfs(b - k, path)
            path.pop()
        
        for i in range(1, 10):
            dfs(i, [])
        return ans