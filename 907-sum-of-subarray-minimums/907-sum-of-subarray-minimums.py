class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        prevMin = [0 for i in range(len(arr))]
        nextMin = [len(arr) - 1 for i in range(len(arr))]
        decStack, incStack = [], []
        # Find the index of the next minimum for each element
        for i in range(len(arr)):
            while incStack and arr[i] <= arr[incStack[-1]]:
                nextMin[incStack.pop()] = i - 1
            incStack.append(i)
            
        # Find the index of the previous minimum for each element
        for i in range(len(arr) - 1, -1, -1):
            while decStack and arr[i] < arr[decStack[-1]]:
                prevMin[decStack.pop()] = i + 1
            decStack.append(i)
        
        ans = n = 0
        for i, j in zip(prevMin, nextMin):
            total = ((j - i + 1) * (j - i + 2)) // 2
            after = ((j - n) * (j - n + 1)) // 2
            before = ((n - i) * (n - i + 1)) // 2
            currentRange = total - after - before
            # print(i, j, total, after, before, currentRange)
            ans += currentRange * arr[n]
            n += 1
        return ans % (10 ** 9 + 7)