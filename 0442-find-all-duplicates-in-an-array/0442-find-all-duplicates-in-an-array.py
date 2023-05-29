class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        res = []
        for i in nums:
            if nums[abs(i)-1] < 0:
                res.append(abs(i))
            else:
                nums[abs(i)-1] *= -1
        return res
        
        '''
        res = {}
        ans = []
        for i in nums:
            if i in res:
                ans.append(i)
            else:
                res[i] = 1
        return ans
        '''