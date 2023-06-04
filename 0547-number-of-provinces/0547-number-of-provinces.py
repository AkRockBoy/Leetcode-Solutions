class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        count = 0
        visited = set()
        def dfs(city):
            visited.add(city)
            for j in range(len(isConnected[city])):
                if isConnected[city][j] == 1 and j not in visited:
                    dfs(j)
                
        for i in range(len(isConnected)):
            if i not in visited:
                dfs(i)
                count += 1
        return count
        