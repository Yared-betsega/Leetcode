class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        ans = set()
        def backtrack(b, path):
            path.append(b)
            if len(path) == n:
                ans.add(int("".join(map(str, path))))
            else:
                if b + k <= 9:
                    backtrack(b + k, path)
                if b - k >= 0:
                    backtrack(b - k, path)
            path.pop()
        
        for i in range(1, 10):
            backtrack(i, [])
        return ans