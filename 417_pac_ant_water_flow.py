class Solution:
    def pacificAtlantic(self, heights):
        
        h = len(heights)
        w = len(heights[0])
        
        #  place holders for outputs
        pac_coord = set()
        ant_coord = set()
        
        # initiate start values
        pac_start = []
        ant_start = []
        
        # populate start vals
        
        for r in range(h):
            pac_start.append((r,0))
            ant_start.append((r,w-1))
            
        for c in range(w):
            pac_start.append((0,c))
            ant_start.append((h-1,c))
        
        # create dfs
        
        def dfs(r,c,out_set,height):
            if (r,c) not in out_set:
                out_set.add((r,c))
            dir = [(r,c+1),(r,c-1),(r+1,c),(r-1,c)]
            for r,c in dir:
                if 0 <=r < h and 0 <= c < w  and (r,c) not in out_set:
                    if heights[r][c] >= height:
                        dfs(r,c,out_set,heights[r][c])
                
        #  call dfs on start values
        for r,c in pac_start: dfs(r,c,pac_coord,heights[r][c])
        for r,c in ant_start: dfs(r,c,ant_coord,heights[r][c])
        
        
        # return the intersection of pac_start and ant_start
        
        return pac_coord & ant_coord
        
        
        
        


heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
obj = Solution()
print(obj.pacificAtlantic(heights))
