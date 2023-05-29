class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) ->int:
        res = Counter(nums[:k])
        sm = sum(nums[:k])
        mx = 0
        if len(res) == k: mx = sm
        for i in range(k,len(nums)):
            sm += nums[i] - nums[i-k]
            res[nums[i]] += 1
            res[nums[i-k]] -= 1
            if res[nums[i-k]] == 0:
                del res[nums[i-k]]
            if len(res) == k:
                mx = max(sm , mx)
        return mx


        '''
        Time Limit Exceeded

        res = []
        i = 0
        mx = 0
        while i < len(nums):
            while len(set(res)) != k and i < len(nums):
                if nums[i] not in res:
                    res.append(nums[i])
                else:
                    res.pop(0)
                    res.append(nums[i])
                i += 1
            if len(set(res)) == k:
                mx = max(mx,sum(set(res)))
            res.pop(0)
        return mx
        '''
                
            