class Solution:
    def pacificAtlantic(self, heights):
        
        h = len(heights)
        w = len(heights[0])
        self.pacific_output = []
        self.atlantic_output =[]
        def flow(r1,c1,r,c,h):
            if r == 0 or c== 0:
                    self.pacific_output.append([r1,c1])
            if r == h-1 or c == w-1:
                    self.atlantic_output.append([r1,c1])
            directions = [(r,c+1),(r+1,c),(r-1,c),(r,c-1)]
            for r,c in directions:
                if 0 <= r < h and 0 <= c <w :
                    if heights[r][c]<= h:
                        flow(r1,c1,r,c,heights[r][c])
                else:return

        # iterate over land cells
        for r in range(h):
            for c in range(w):
                flow(r,c,r,c,heights[r][c])
        
        intersct = [value for value in self.pacific_output if value in self.atlantic_output]
                
        return intersct
        
        
        
        
        


heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
obj = Solution()
print(obj.pacificAtlantic(heights))

[[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]
[[1, 2], [1, 3], [2, 1], [2, 2], [3, 1]]

[[0, 0], [0, 1], [0, 1], [0, 4], [1, 0], [1, 0], [1, 0], [1, 2], [1, 3], [1, 3], [2, 1], [2, 2], [2, 2], [3, 0], [3, 0], [3, 0], [3, 1], [3, 1], [3, 1], [3, 1], [4, 0]]