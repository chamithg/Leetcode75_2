class Solution:
    def findBall(self, grid):
        
        h = len(grid)
        w = len(grid[0])
        falling_pos = []
        
        for i in range(w):
            falling_pos.append(i)
            
        # determine paths from bottem
        def find_stat(ball_col):
            for i in grid:
                if i [ball_col] ==1:
                    if ball_col == w-1 or i[ball_col+1] == -1: 
                        return -1
                    
                    else: ball_col +=1
                elif i [ball_col] ==-1:
                    if ball_col == 0 or i[ball_col-1] == 1: 
                        return -1
                    else: ball_col -=1
            return ball_col
        
        for i in range(len(falling_pos)):
            falling_pos[i] = find_stat(i)           

        return falling_pos
        

grid = [[1,1,1,-1,-1],[1,1,1,-1,-1],[-1,-1,-1,1,1],[1,1,1,1,-1],[-1,-1,-1,-1,-1]]
obj = Solution()
print(obj.findBall(grid))