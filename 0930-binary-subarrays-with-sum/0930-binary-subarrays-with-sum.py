class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        def fun(nums,sm):
            if sm < 0: return 0
            presum = i = j = count = 0
            for i in range(len(nums)):
                presum += nums[i]
                while presum > sm:
                    presum -= nums[j]
                    j += 1
                count += i- j + 1
            return count

        return fun(nums,goal) - fun(nums,goal-1)

        '''
        count = 0
        ans = {0:1}
        sm = 0
        for i in nums:
            sm += i
            if sm - goal in ans:
                count += ans[sm - goal]
            ans[sm] = ans.get(sm,0) + 1
        return count
'''
            

        '''
        n = len(nums)
        if goal == 0 and len(set(nums)) == 1 and nums[0] == 0: return ((n*(n+1))//2)
        count = 0
        sm = 0
        index = 0
        i = 0
        plusi = 0
        while i < len(nums):
            sm += nums[i]
            if sm == goal:
                count += 1
                j = i
                while j < len(nums)-1 and nums[j+1] != 1:
                    count += 1 
                    j += 1
                while plusi < len(nums) and nums[plusi] != 1:
                    plusi += 1
                    count += 1
                if plusi < len(nums):
                    sm -= nums[plusi]
                plusi += 1
            i += 1
        return count
        '''

                

                    




        