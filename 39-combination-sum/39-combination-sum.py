class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        answer = []
        def helper(total, i, lst):
            if total > target:
                lst.pop()
                return
            if total == target:
                answer.append(lst.copy())
            else:
                for i in range(i, len(candidates)):
                    lst.append(candidates[i])
                    helper(total + candidates[i], i, lst)
            lst.pop()
        
        for i in range(len(candidates)):
            helper(candidates[i], i, [candidates[i]])
        return answer
        