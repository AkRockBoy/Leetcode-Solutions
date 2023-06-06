class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        m,n = [],[]
        output = []
        for i in matrix:
            m.append(min(i))
        for i in range(len(matrix[0])):
            c = []
            for j in range(len(matrix)):
                c.append(matrix[j][i])
            n.append(max(c))
        for i in m:
            if i in n:
                output.append(i)
        return output