class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if k == 1:return nums
        import heapq
        heap , res = [] , []
        for i in range(k):
            heapq.heappush(heap,(-nums[i],i))
        heapq.heapify(heap)
        res.append(-heap[0][0])
        for i in range(k,len(nums)):
            while heap[0][1] <= i-k:
                heapq.heappop(heap)
            heapq.heappush(heap,(-nums[i],i))
            res.append(-heap[0][0])
        return res

        '''
        ans = []
        n = len(nums)
        for i in range(k):
            while ans and nums[i] >= nums[ans[-1]]:
                ans.pop()
            ans.append(i)
        res=[]
        for i in range(k,n):
            res.append(nums[ans[0]])
            while ans and ans[0] <= i-k:
                ans.pop(0)
            while ans and nums[i] >= nums[ans[-1]]:
                ans.pop()
            ans.append(i)
        res.append(nums[ans[0]])
        return res
    '''

    
        '''
        res=[]
        for i in range(0,len(nums)-k+1):
            res.append(max(nums[i:i+k]))
        return res
        '''