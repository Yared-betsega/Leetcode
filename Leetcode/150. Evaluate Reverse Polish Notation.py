import math
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        lst = []
        ops = ["+", "-", "*", "/"]
        for i in tokens:
            if i not in ops:
                lst.append(int(i))
            else:
                
                if i == "+":
                    x = lst[-1] + lst[-2]
                elif i == "-":
                    x = lst[-2] - lst[-1]
                elif i == "*":
                    x = lst[-1] * lst[-2]
                else:
                    x = math.trunc(lst[-2] / lst[-1])
                lst.pop()
                lst.pop()
                lst.append(x)
        return lst[0]
