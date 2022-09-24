class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x: (x[1], x[0]))
        curEnd, ans = intervals[0][1], 0
        for i in range(1, len(intervals)):
            st, end = intervals[i]
            if st < curEnd:
                ans += 1
            else:
                curEnd = end
        return ans
            
# time and space complexity
# time: O(nlogn)
# space: O(1)