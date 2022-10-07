class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        nums = [i for i in range(1, n + 1)]
        path = []
        ans = set()
        def backtrack(i):
            if i != -1:
                path.append(nums[i])
            if len(path) == k:
                ans.add(tuple(sorted(path)))
            else:
                for j in range(i + 1, len(nums)):
                    backtrack(j)
            if i != -1:
                path.pop()
        backtrack(-1)
        return ans