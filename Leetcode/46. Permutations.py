# https://leetcode.com/problems/permutations/

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        graph = defaultdict(list)
        for i in range(len(nums)):
            graph[nums[i]] = nums[:i] + nums[i+1:]
        answer = set()
        def dfs(num, path):
            path.append(num)
            if len(path) == len(nums):
                answer.add(tuple(path))
            else:
                for i in graph[num]:
                    if i not in path:
                        dfs(i, path)
            path.pop()
            
        for num in nums:
            dfs(num, [])
        return answer
                
