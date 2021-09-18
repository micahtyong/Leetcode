class Solution:
    directions = [(1,0),(-1,0),(0,1),(0,-1)]
    
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # path for rain water at cell (r_i, c_i) to flow into both left/up (pacific) and right/down (atlantic)
        # return that list of coordinates meeting these conditions 
        peaks = [] 
        goodPaths = set()
        for r in range(len(heights)):
            for c in range(len(heights[0])):
                req = { 'hitPacific': False, 'hitAtlantic': False, 'seen': set(), 'goodPaths': goodPaths }
                if self.dfs(float('inf'), r, c, heights, req):
                    peaks.append([r, c])
                    goodPaths.add((r, c))
        return peaks
    
    def dfs(self, prevHeight, r, c, heights, req):
        # bases
        inBounds = r >= 0 and r < len(heights) and c >= 0 and c < len(heights[0])
        if not inBounds or heights[r][c] > prevHeight or (r, c) in req['seen']:
            return False
        if (r, c) in req['goodPaths']: # cache 
            req['hitPacific'] = True
            req['hitAtlantic'] = True
        if r == 0 or c == 0:
            req['hitPacific'] = True
        if r == (len(heights) - 1) or c == (len(heights[0]) - 1):
            req['hitAtlantic'] = True
        if req['hitPacific'] and req['hitAtlantic']: 
            return True
        
        # travel (condition on directions)
        currHeight = heights[r][c]
        req['seen'].add((r, c))
        self.dfs(currHeight, r + 1, c, heights, req) # down
        self.dfs(currHeight, r - 1, c, heights, req) # up
        self.dfs(currHeight, r, c - 1, heights, req) # left
        self.dfs(currHeight, r, c + 1, heights, req) # right
        
        return req['hitPacific'] and req['hitAtlantic']