class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        row_counts = defaultdict(int)
        count = 0
        for row in grid:
            row_counts[tuple(row)] += 1
        
        for column in zip(*grid):
            count += row_counts[column]
            
        return count
        '''
        n = len(grid)
        count = 0
        for i in range(n):
            for j in range(n):
                for k in range(n):
                    if grid[i][k] != grid[k][j]:
                        break
                else:
                    count += 1
        return count
        '''