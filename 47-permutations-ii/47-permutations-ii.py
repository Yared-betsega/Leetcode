class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        graph = defaultdict(list)
        for i in range(len(nums)):
            graph[i] = [m for m in range(len(nums)) if m != i]
        answer = set()
        def dfs(i, path):
            path.append(i)
            if len(path) == len(nums):
                answer.add(tuple([nums[j] for j in path]))
            else:
                for j in graph[i]:
                    if j not in path:
                        dfs(j, path)
            path.pop()
            
        for i in range(len(nums)):
            dfs(i, [])
        return answer
                
            