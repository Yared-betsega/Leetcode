class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x: (x[0], -x[1]))
        stack = [intervals[0]]
        for i in range(1, len(intervals)):
            if stack[-1][0] <= intervals[i][0] and intervals[i][1] <= stack[-1][1]:
                continue
            stack.append(intervals[i])
        
        return len(stack)

# time and space complexity
# time: O(n)
# space: O(n)