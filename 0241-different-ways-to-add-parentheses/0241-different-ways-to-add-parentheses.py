class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
                
        def recursion(exp):
            res=[]
            for i in range(len(exp)):
                if exp[i]=='+' or exp[i]=='-' or exp[i]=='*':
                    left=recursion(exp[:i])
                    right=recursion(exp[i+1:])
                    for l in left:
                        for r in right:
                            res.append(eval(str(l) + exp[i] + str(r)))
            if not res:
                res.append(int(exp))
            
            return res
        
        return recursion(expression)