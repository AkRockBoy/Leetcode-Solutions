class Solution:
    def findNonMinOrMax(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return -1
        mn = mx = nums[0]
        for i in range(1,len(nums)):
            mn = min(mn, nums[i])
            mx = max(mx, nums[i])

        for num in nums:
            if num != mn and num != mx:
                return num
        return -1