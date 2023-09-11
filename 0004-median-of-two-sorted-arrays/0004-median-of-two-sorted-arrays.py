class Solution:
    def findMedianSortedArrays(self, l1: List[int], l2: List[int]) -> float:
        l3=l1[:]+l2[:]
        l=len(l3)
        l3.sort()
        if l%2!=0:
            res=l3[int(l/2)]
        else:
            midan1=l3[int(l/2)]
            midan2=l3[int(l/2)-1]
            res=(midan1+midan2)/2
        return res
        