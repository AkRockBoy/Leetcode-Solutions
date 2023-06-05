class Solution:
    def checkStraightLine(self, l: List[List[int]]) -> bool:
        x0 , y0 = l[0][0] , l[0][1]
        x1 , y1 = l[1][0] , l[1][1]
        dx = x1 - x0 
        dy = y1 - y0
        for i in range(len(l)):
            x , y = l[i][0] , l[i][1]
            if dx * (y - y1) != dy * (x - x1):
                return False
        return True
            