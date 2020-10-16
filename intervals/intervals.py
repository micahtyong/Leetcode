def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
    # Sort intervals based on starting key
    sortedIntervals = sorted(intervals, key=lambda x: x[0])
    mergeIndex = 0
    erases = 0

    # Identify overlapping intervals
    while mergeIndex < (len(sortedIntervals) - 1):
        a_start, a_end = sortedIntervals[mergeIndex]
        b_start, b_end = sortedIntervals[mergeIndex + 1]
        begin_overlap = a_start <= b_start and b_start < a_end
        if begin_overlap:
            erases += 1
        else:
            mergeIndex += 1
    return erases


def merge(self, intervals: List[List[int]]) -> List[List[int]]:
    # Sort intervals based on starting key
    sortedIntervals = sorted(intervals, key=lambda x: x[0])
    mergeIndex = 0
    # Combine and prune overalapping intervals in sortedIntervals
    while mergeIndex < (len(sortedIntervals) - 1):
        a_start, a_end = sortedIntervals[mergeIndex]
        b_start, b_end = sortedIntervals[mergeIndex + 1]
        begin_overlap = a_start <= b_start and b_start <= a_end
        if begin_overlap:
            sortedIntervals[mergeIndex][1] = max(a_end, b_end)  # Merge
            sortedIntervals.pop(mergeIndex + 1)  # Prune
        else:
            mergeIndex += 1
    return sortedIntervals
