class Solution:
    def matrixSumQueries(self, n: int, queries: List[List[int]]) -> int:
        col = set()
        row = set()
        q = len(queries)
        ans = 0
        for idx in range(q-1, -1, -1):
            t, i, v = queries[idx]
            if t == 1:
                if i not in col:
                    ans += v * (n - len(row))
                    col.add(i)
            else:
                if i not in row:
                    ans += v * (n - len(col))
                    row.add(i)
        return ans
        '''
        res = [[0]*n for i in range(n)]
        for m in queries:
            typei , indexi , vali = m
            if typei == 0:
                for i in range(n):
                    res[indexi][i] = vali
            elif typei == 1:
                for j in range(n):
                    res[j][indexi] = vali
        sm = 0
        for i in range(n):
            for j in range(n):
                sm+=res[i][j]
        return sm
        '''
        