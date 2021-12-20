def merge(intervals):
    if len(intervals) <= 1:
        return intervals
    mergedIntervals = []
    mergedIntervals.append(intervals[0])
    length = len(intervals)
    for i in range(1, length):
        if intervals[i][0] <= mergedIntervals[-1][1]:
                if intervals[i][1] >= mergedIntervals[-1][1]:
                    mergedIntervals[-1][1] = intervals[i][1]
        else:
            mergedIntervals.append(intervals[i])
    return mergedIntervals

