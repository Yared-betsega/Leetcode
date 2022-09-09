class Solution:
    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
        properties.sort(key = lambda x: (x[0], -x[1]))
        stack, ans = [], 0
        for i in range(len(properties)):
            while stack and properties[i][0] > stack[-1][0] and properties[i][1] > stack[-1][1]:
                stack.pop()
                ans += 1
            stack.append(properties[i])
        return ans

# time and space complexity
# time: O(n)
# space: O(n)