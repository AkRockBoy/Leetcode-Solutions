class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        n , res = len(nums) , set()
        for i in range(n+1):
            for j in range(i+1,n+1):
                left , right = j + 1 , n - 1
                while left < right:
                    if nums[i] + nums[j] + nums[left] + nums[right] == target:
                        res.add((nums[i] , nums[j] , nums[left] , nums[right]))
                        right -= 1
                        left += 1
                    elif nums[i] + nums[j] + nums[left] + nums[right] < target:
                        left += 1
                    else:
                        right -= 1
        return res
        