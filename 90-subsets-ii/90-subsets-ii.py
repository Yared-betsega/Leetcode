class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans = set([()])
        path = []
        def backtrack(i):
            if i != -1:
                path.append(nums[i])
                ans.add(tuple(sorted(path)))
            for j in range(i + 1, len(nums)):
                backtrack(j)
            if i != -1:
                path.pop()
        backtrack(-1)
        return ans