class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
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

