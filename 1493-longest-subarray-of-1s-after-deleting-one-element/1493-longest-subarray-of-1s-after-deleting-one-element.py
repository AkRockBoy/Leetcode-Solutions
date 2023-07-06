class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        res = 0
        k = 1
        l = 0
        for r in range(len(nums)):
            if nums[r] == 0:
                k -= 1
            while k < 0 and l <= r:
                if nums[l] == 0:
                    k += 1
                l += 1
            res = max(res, r-l)
        return res

        '''
        if len(set(nums)) == 1:
            if nums[0] == 0: return 0
            return len(nums)-1
        if len(nums) == 1:
            if nums[0] == 0: return 0
            return 1
        countzero = nums.count(0)
        if countzero == 1: return len(nums) -1 
        res = []
        res.append(0)
        for i in range(1,len(nums)-1):
            if nums[i] == 0:
                res.append(i)
        res.append(len(nums)-1)
        i = 1 
        j = 0
        mx = 0
        while i < len(res):
            if i == 1:
                mx = max(mx,res[i]-1)
            else:
                mx = max(mx, res[i]-res[j] - 2)
                j += 1
            i += 1
        return mx
                   ''' 
    
