class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        '''
        if not grid:return 0
        
        count = 0
        def dfs(grid, i, j):
            if i<0 or j<0 or i>=len(grid) or j>=len(grid[0]) or grid[i][j] != '1':return
            grid[i][j] = 'x'
            dfs(grid, i+1, j)
            dfs(grid, i-1, j)
            dfs(grid, i, j+1)
            dfs(grid, i, j-1)
            
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    dfs(grid, i, j)
                    count += 1
        return count

        
        '''
        if not grid:return 0
        count = 0 
        n , m = len(grid) , len(grid[0])
        
        def dfs(grid , row , col):
            if row < 0 or row >= n or col < 0 or col >= m or grid[row][col] != "1":return
            
            grid[row][col] = "x"
            
            dfs(grid,  row-1 , col)
            dfs(grid , row+1 , col)
            dfs(grid , row , col-1)
            dfs(grid , row , col+1)
            
        for i in range(n):
            for j in range(m):
                if grid[i][j] == "1":
                    dfs(grid , i , j)
                    count += 1
        return count
                    