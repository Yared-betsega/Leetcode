class Solution:
    def calculate(self, s: str) -> int:
        disIntegrated = list(filter(lambda x: x != " ", list(s)))
        expression = []
        prev = ""
        for i in range(len(disIntegrated)):
            if disIntegrated[i].isdigit():
                prev += disIntegrated[i]
                if i == len(disIntegrated) - 1:
                    expression.append(prev)
            else:
                if len(prev) > 0:
                    expression.append(prev)
                    prev = ""
                expression.append(disIntegrated[i])
                
                
        def solve(exp):
            
            if exp[0] == "-":
                exp[1] = -exp[1]
                exp.pop(0)
                
            stack = []
            ops = ["-", "+"]
            for i in range(len(exp)):
                if stack and stack[-1] in ops:
                    op = stack.pop()
                    first = stack.pop()
                    second = exp[i]
                    stack.append(first + second if op == "+" else first - second)
                else:
                    stack.append(exp[i])
            
            return stack[0] 
                
        stack = []
        for i in range(len(expression)):
            if expression[i] == ")":
                temp = []
                while stack and stack[-1] != "(":
                    temp.append(stack.pop())
                stack.pop()
                stack.append(solve(temp[::-1]))
            else:
                if expression[i].isdigit():
                    stack.append(int(expression[i]))
                else:
                    stack.append(expression[i])
                    
        return solve(stack)
                