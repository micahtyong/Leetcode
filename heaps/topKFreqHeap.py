# same runtime as sorting a list ...
from heapq import heapify, heappop
from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # pq solution
        # create mapping from digit -> num_occurrences // o(n)
        digitToOc = defaultdict(int)
        for num in nums: 
            digitToOc[num] += 1
        # create heap // o(n log)
        heap = list(map(lambda x: (-x[1], x[0]), digitToOc.items())) # negate freq to make max heap
        heapify(heap) # nlogn
        # pop off k
        ret = []
        for i in range(k):
            ret.append(heappop(heap)[1])
        return ret
        