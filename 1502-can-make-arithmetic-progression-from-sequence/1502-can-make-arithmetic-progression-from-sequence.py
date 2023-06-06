class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        arr.sort()
        res=abs(arr[0]-arr[1])
        for i in range(1,len(arr)-1):
            if res != abs(arr[i]-arr[i+1]):
                return False
        return True
