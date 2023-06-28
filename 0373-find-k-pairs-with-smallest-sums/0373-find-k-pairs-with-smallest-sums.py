class Solution:
    import heapq
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        n1, n2 = len(nums1), len(nums2)
        if not nums1 or not nums2:
            return []
        heap = [(nums1[i] + nums2[0], i, 0) for i in range(n1)]
        heapq.heapify(heap)
        res = []
        while k > 0 and heap:
            s, i, j = heapq.heappop(heap)
            res.append([nums1[i], nums2[j]])
            if j + 1 < n2:
                heapq.heappush(heap, (nums1[i] + nums2[j+1], i, j + 1))
            k -= 1
        return res
        
        '''
        heap = []
        for i in nums1:
            for j in nums2:
                heapq.heappush(heap,(i+j,i,j))
        res = []
        for i in range(min(k,len(heap))):
            j , num1 , num2 = heapq.heappop(heap)
            res.append([num1,num2])
        return res
        


        heap = []
        for i in range(len(nums1)):
            for j in range(len(nums2)):
                heapq.heappush(heap,(-(nums1[i]+nums2[j]),[nums1[i],nums2[j]]))
                if len(heap) > k: heapq.heappop(heap)    
        ans = []
        for key  , pair in heap:
            ans.append(pair)
        return ans
            



        res = []
        for i in range(len(nums1)):
            for j in range(len(nums2)):
                res.append([nums1[i],nums2[j]])
        heap = []
        for i in range(len(res)):
            heapq.heappush(heap,(-(sum(res[i])),res[i]))
            if len(heap) > k:
                heapq.heappop(heap)
        ans = []
        for key  , pair in heap:
            ans.append(pair)
        return ans
            


        res = []
        for i in range(len(nums1)):
            for j in range(len(nums2)):
                res.append([nums1[i],nums2[j]])
        res = sorted(res, key = lambda x:sum(x))
        return res[:k]
            '''
            
                
        