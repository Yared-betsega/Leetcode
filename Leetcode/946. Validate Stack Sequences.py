def validateStackSequences(pushed, popped):
        stack = []
        ans = []
        j = 0
        for i in range(len(pushed)):
            stack.append(pushed[i])
            
            while stack and stack[-1] == popped[j]:
                ans.append(stack.pop())
                j += 1
        if ans == popped:
            return True
        return False
