class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        res = maxsize
        left , sm = 0 , 0
        for i in range(len(nums)):
            sm += nums[i]
            while sm >= target:
                res = min( res, i - left + 1)
                sm -= nums[left]
                left += 1
        if res == maxsize:return 0
        return res



        '''
        i , j = 0 , 0
        sm = 0
        mx = float('inf')
        while i < len(nums):
            if sm < target and j < len(nums):
                sm += nums[j]
                j += 1
            else:
                if sm >= target:
                    mx = min(mx , j-i)
                    sm -= nums[i]
                    i += 1
                else:
                    break 
        if mx == float('inf'): return 0
        return mx

'''

            




