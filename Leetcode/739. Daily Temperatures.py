def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        ans = []
        stack.append(0)
        ans.append(0)
        for i in range(1, len(temperatures)):
            if temperatures[i] < temperatures[stack[-1]]:
                stack.append(i)
                ans.append(0)
            else:
                while stack and temperatures[i] > temperatures[stack[-1]]:
                    last = stack.pop()
                    x = i - last
                    ans[last] = x
                stack.append(i)
                ans.append(0)
                
        return ans
