class Solution:
    def findCenter(self, arr: List[List[int]]) -> int:
        return list(set(arr[0]).intersection(set(arr[1])))[0]
        
        