from collections import defaultdict

# o(n) means we cant sort the length n array, since that would take o(n log n) 

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # create an edge if it has a before or after
        # directed edge in increasing order
        elems = set(nums)
        adj_list = defaultdict(list)
        
        for num in elems:
            if num + 1 in elems:
                adj_list[num].append(num + 1)
                
        # will need a cache for o(n)
        visited = defaultdict(int)
        maxLen = 0
        for num in elems: 
            curr = self.dfs(adj_list, visited, num)
            if curr > maxLen:
                maxLen = curr
                
        return maxLen
            
        

    def dfs(self, adj_list, visited, i): 
        if i in visited: 
            return visited[i]
        visited[i] += 1
        for neighbor in adj_list[i]: # max of one
            visited[i] += self.dfs(adj_list, visited, neighbor)
        
        return visited[i]
        