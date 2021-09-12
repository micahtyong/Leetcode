import heapq
from collections import defaultdict

# o(n log n)
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # create mapping from digit -> num_occurrences
        digitToOc = defaultdict(int)
        for num in nums: 
            digitToOc[num] += 1
        # extract sorted list
        sortedLst = sorted(digitToOc.items(), key = lambda x: x[1])
        # return last k
        return list(map(lambda x: x[0], sortedLst[len(sortedLst) - k:]))