class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        '''   SOLVED USING RECURSION  ''' 
        '''
        nums.sort()
        @lru_cache(None)
        def fun(target):
            if target == 0: return 1
            if target < 0: return 0
            count = 0
            for i in nums:
                if target - i >= 0:
                    count += fun(target - i)
            return count
        return fun(target)
        '''
            
        '''  SOLVED USING MEMOIZATION ''' 
     
        nums.sort()
        memo = {}
        def fun(target , memo):
            if target in memo: return memo[target]
            if target == 0: return 1
            if target < 0: return 0
            count = 0
            for i in nums:
                if target - i >= 0:
                    count += fun(target - i , memo)
            memo[target] = count
            return count
        return fun(target , memo)
            