class Solution:
    def deleteGreatestValue(self, grid: List[List[int]]) -> int:
        res = []
        for i in grid:
            res.append(sorted(i)[::-1])
        print(res)
        sm = 0
        for j in range(len(res[0])):
            mx = float('-inf')
            for i in range(len(res)):
                mx = max(res[i][j],mx)
            sm += mx
        return sm
            
        