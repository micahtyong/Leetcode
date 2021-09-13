class Solution:
    # target = a + b;; b = target - a
    # invariant := only one solution (unique key)
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        buf = {} #  target - a = b -> index of b 
        for i, b in enumerate(nums):
            a = target - b
            if a in buf: # value match
                return [buf[a], i] # index of "a", index of "b" 
            else: 
                buf[b] = i # b = target - a -> index of b
                