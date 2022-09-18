class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        answer = []
        
        def helper(o, c, sec):
            if c == n:
                answer.append(sec)
                return 
            elif o < n and c == o:
                sec += '('
                helper(o + 1, c, sec)
            elif o == n and c < n:
                sec += ')'
                helper(o, c + 1, sec)
            else:
                helper(o + 1, c, sec + '(' )
                helper(o, c + 1, sec + ')')
        
        helper(0, 0, '')
        return answer
                