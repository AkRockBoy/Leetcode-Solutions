class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        ones = 0 
        index = 0
        for i, row in enumerate(mat):
            c = row.count(1)
            if ones < c:
                ones = c
                index = i
        return [index,ones]
    '''
        res = []
        count = 0
        for i in mat:
            if 1 in i:
                one = i.count(1)
                index = count
                count += 1
                res.append([one,index])
            else:
                res.append([0,count])
                count += 1
        res.sort()
        mxo = 0
        mxindex = 0
        for one , index in res:
            if one > mxo:
                mxo = one
                mxindex = index
        return [mxindex,mxo]

'''