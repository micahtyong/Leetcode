from heapq import heapify, heappop
from collections import defaultdict
# hello

class Solution: # o(n). in practice is ok... 
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # bucket sort
        bucket = [[] for _ in range(len(nums) + 1)] # n + 1 buckets
        Count = Counter(nums).items()  # default dict with frequencies... cleaner than defaultdict
        for num, freq in Count: bucket[freq].append(num) # o(n) time
        flat_list = list(chain(*bucket)) # destructures bucket k
        return flat_list[len(flat_list) - k:]
        