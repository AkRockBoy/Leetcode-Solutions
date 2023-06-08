class Solution:
    def countNegatives(self, l: List[List[int]]) -> int:
        n=len(l[0])
        row=len(l)-1
        col=0
        count=0
        while row >= 0 and col < n:
            if l[row][col] < 0:
                count += n-col
                row-=1
            else:
                col+=1
        return count
            