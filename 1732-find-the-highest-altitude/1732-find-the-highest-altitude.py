class Solution:
    def largestAltitude(self, nums: List[int]) -> int:
        res=[0]*(len(nums)+1)
        res[1] = nums[0] 
        for i in range(1,len(nums)):
            res[i+1] = res[i] + nums[i]
        return max(res)
