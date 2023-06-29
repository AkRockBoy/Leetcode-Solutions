class Solution:
    import heapq
    def minimumOperations(self, nums: List[int]) -> int:
        count = 0
        heapq.heapify(nums)
        while sum(nums) != 0:
            num = heapq.heappop(nums)
            while num == 0:
                num = heapq.heappop(nums)
            nums = [ i-num for i in nums]
            count += 1
        return count 
        '''
        import heapq
        heap = []
        for i in nums:
            if i != 0:
                heapq.heappush(heap,i)
        count = 0
        while heap:
            num = heapq.heappop(heap)
            while heap and num == heap[0]:
                heappop(heap)
            count += 1
            for i in range(len(heap)):
                heap[i] -= num
        return count
'''
