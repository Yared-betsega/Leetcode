class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        if n > 45:
            return []
        
        ans = set()
        def backtrack(i, total, lst):
            lst.append(i)
            total += i
            if total == n:
                if len(lst) == k:
                    ans.add(tuple(lst))
                return 
            if total < n:
                for j in range(i + 1, 10):
                    backtrack(j, total, lst.copy())
            total -= lst.pop()
        for i in range(1, 10):
            backtrack(i, 0, [])
        return ans