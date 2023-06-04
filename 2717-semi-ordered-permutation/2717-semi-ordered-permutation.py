class Solution:
    def semiOrderedPermutation(self, nums: List[int]) -> int:
        n = len(nums)
        start = nums.index(1)
        end = nums.index(n)
        if end > start :
            return (start-0) + (n-1-end)
        else:
            return (start-0) + (n-1-end) - 1
        
        
        
        '''
        n = len(nums)
        if nums[0] == 1 and nums[n-1] == n:return 0
        start = nums.index(1)
        if start == 0:
            end = nums.index(n)
            if end == n-1:
                return count
            else:
                return n-1-end
        else:
            count = 0
            while nums[0] != 1:
                nums[start] , nums[start-1] = nums[start-1],nums[start]
                start -= 1
                count += 1
            end = nums.index(n)
            if end == n-1: return count
            else:
                return count + n-1-end
                
                
                '''
        
        