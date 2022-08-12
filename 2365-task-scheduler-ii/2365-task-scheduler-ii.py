class Solution:
    def taskSchedulerII(self, tasks: List[int], space: int) -> int:
        entry = {}
        for task in tasks:
            entry[task] = -space
        days = 0
        for task in tasks:
            if days - entry[task] >= space:
                days += 1
            else:
                days += space - (days - entry[task]) + 1
            entry[task] = days
        return days

# time and space complexity
# time: O(n)
# space: O(n)