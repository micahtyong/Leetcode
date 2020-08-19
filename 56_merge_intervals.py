class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        sortedIntervals = sorted(intervals, key=lambda x: x[0])
        mergeIndex = 0
        while mergeIndex < (len(sortedIntervals) - 1):
            a_start, a_end = sortedIntervals[mergeIndex]
            b_start, b_end = sortedIntervals[mergeIndex + 1]
            begin_overlap = a_start <= b_start and b_start <= a_end
            if begin_overlap:
                sortedIntervals[mergeIndex][1] = max(a_end, b_end)
                sortedIntervals.pop(mergeIndex + 1)
            else:
                mergeIndex += 1
        return sortedIntervals
