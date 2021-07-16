import operator
class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        intervals = sorted(intervals, key = operator.itemgetter(1)) #
        minIntervals = mergeIndex = 0 #
        while mergeIndex < len(intervals) - 1:
            if (intervals[mergeIndex][1] > intervals[mergeIndex + 1][0]):
                minIntervals += 1 #
                intervals.pop(mergeIndex + 1) 
            else: 
                mergeIndex += 1
        return minIntervals