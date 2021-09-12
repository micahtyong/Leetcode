import bisect
from heapq import heappush, heappop

class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        # invariant: small half, large half
        self.total = 0
        self.small = [] # smaller half of list (max-heap)
        self.large = [] # larger half of list (min-heap)
        

    def addNum(self, num: int) -> None:
        if len(self.small) == len(self.large):
            heappush(self.small, -num)
            heappush(self.large, -heappop(self.small))
        else:
            heappush(self.large, num)
            heappush(self.small, -heappop(self.large))
        

    def findMedian(self) -> float:
        if len(self.small) == len(self.large):
            return (self.large[0] - self.small[0]) / 2
        else:
            return self.large[0]
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()