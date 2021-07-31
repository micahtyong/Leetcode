# https://leetcode.com/problems/combination-sum/

class Solution(object):
    # Learnings: Not everything is binary (curr or next)
    # When possible (esp for DFS), iterate through the list! (this, next, next next...)
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        combos = []
        def dfs(candidates, target, combo = []):
            if not candidates or target < 0: 
                return
            if target == 0: 
                combos.append(combo)
                return
            for i in range(len(candidates)):
                dfs(candidates[i:], target - candidates[i], combo + [candidates[i]])
        dfs(candidates, target)
        return combos
            