class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        answer = set()
        def backtrack(i, path):
            if i >= len(s):
                answer.add(path)
                return
            if s[i].isdigit():
                backtrack(i + 1, path + s[i])
            else:
                backtrack(i + 1, path + s[i].upper())
                backtrack(i + 1, path + s[i].lower())
        
        backtrack(0, "")
        return answer