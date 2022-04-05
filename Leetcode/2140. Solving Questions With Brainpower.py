# https://leetcode.com/problems/solving-questions-with-brainpower/

class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        
        def helper(cur, memo):
            if cur > len(questions) - 1:
                return 0
            if cur in memo:
                return memo[cur]
            
            solved = questions[cur][0] + helper(cur + questions[cur][1] + 1, memo)
            notSolved = helper(cur + 1, memo)
            memo[cur] = max(solved, notSolved)
            return memo[cur]
        
        return helper(0, {})
            
# time and space complexity
# time complexity = O(n)
# space complexity = O(n)
