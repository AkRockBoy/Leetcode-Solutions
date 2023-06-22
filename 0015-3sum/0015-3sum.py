class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res , n = set() , len(nums)-1
        nums.sort()
        for i in range(len(nums)):
            left = i + 1
            right = n
            while left < right:
                if nums[i] + nums[left] + nums[right] == 0:
                    res.add((nums[i],nums[left],nums[right]))
                    left += 1
                    right -= 1
                elif nums[i] + nums[left] + nums[right] < 0:
                    left += 1
                else:
                    right -= 1
        return res


        
        