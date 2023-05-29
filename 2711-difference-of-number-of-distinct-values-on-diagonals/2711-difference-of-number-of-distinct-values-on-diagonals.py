class Solution:
    def differenceOfDistinctValues(self, grid: List[List[int]]) -> List[List[int]]:
        def fun1(grid):
            m, n = len(grid), len(grid[0])
            top_left_diagonal = [[0] * n for _ in range(m)]
            for r in range(m):
                for c in range(n):
                    values = set()
                    i, j = r-1, c-1
                    while i >= 0 and j >= 0:
                        values.add(grid[i][j])
                        i -= 1
                        j -= 1
                    top_left_diagonal[r][c] = len(values)
            return top_left_diagonal


        def fun2(grid):
            m, n = len(grid), len(grid[0])
            bottom_right_diagonal = [[0] * n for _ in range(m)]
            for r in range(m):
                for c in range(n):
                    values = set()
                    i, j = r+1, c+1
                    while i < m and j < n:
                        values.add(grid[i][j])
                        i += 1
                        j += 1
                    bottom_right_diagonal[r][c] = len(values)
            return bottom_right_diagonal


        def solve(grid):
            m, n = len(grid), len(grid[0])
            answer = [[0] * n for _ in range(m)]

            top_left_diagonal = fun1(grid)
            bottom_right_diagonal = fun2(grid)

            for r in range(m):
                for c in range(n):
                    answer[r][c] = abs(top_left_diagonal[r][c] - bottom_right_diagonal[r][c])
            return answer

        return solve(grid)