class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        graph = {}
        for i in range(len(nums)):
            graph[nums[i]] = nums[i+1:]
        subsets = [[]]
        def dfs(i, cur):
            cur.append(i)
            subsets.append(cur[:])
            for j in graph[i]:
                dfs(j, cur)
            cur.pop()
        for num in nums:
            dfs(num, [])
        return subsets