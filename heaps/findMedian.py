# https://leetcode.com/problems/find-median-from-data-stream/submissions/
import bisect

class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.lst = []
        

    def addNum(self, num: int) -> None:
        bisect.insort(self.lst, num)
        

    def findMedian(self) -> float:
        # even nums 
        medianIndex = int(round((len(self.lst) / 2) - 0.001))
        print(medianIndex)
        if len(self.lst) % 2 == 0:
            return (self.lst[medianIndex] + self.lst[medianIndex - 1]) / 2
        else:
            return self.lst[medianIndex]
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()