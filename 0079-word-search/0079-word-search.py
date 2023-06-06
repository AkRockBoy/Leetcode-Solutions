class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        n = len(board)
        m = len(board[0])
        
        def dfs(r , c , index):
            if index == len(word):
                return True
            if r < 0 or r >= n or c < 0 or c >= m or board[r][c] != word[index]: return False
            ch = board[r][c]
            board[r][c] = '#'
            res = dfs(r + 1 , c , index + 1) or dfs(r - 1 , c , index + 1) or dfs(r , c + 1 , index + 1) or dfs(r , c - 1 , index + 1)
            board[r][c] = ch
            return res
        
        for i in range(n):
            for j in range(m):
                if (dfs(i,j,0)):
                    return True
        return False
                    
        