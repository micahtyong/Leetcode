class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1: 
            return nums[0]
        rob_map_first, rob_map_last = {}, {}
        def helper(nums, rob_map):
            if len(nums) == 0: 
                return 0
            if len(nums) in rob_map:
                return rob_map[len(nums)]
            rob_this = nums[0] + helper(nums[2:], rob_map)
            rob_next = helper(nums[1:], rob_map)
            best_rob = max(rob_this, rob_next)
            rob_map[len(nums)] = best_rob
            return best_rob
        return max(helper(nums[:-1], rob_map_first), helper(nums[1:], rob_map_last))