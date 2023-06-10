class Solution:
    def sumDistance(self, nums: List[int], s: str, d: int) -> int:
        pos = list(nums)
        for i in range(len(nums)):
            if s[i] == 'L':
                pos[i] -= d
            else:
                pos[i] += d
        prev = 0 
        ans = 0
        pos.sort()
        for i in range(1,len(pos)):
            ans += (i*(abs(pos[i] - pos[i-1]))+ prev)
            prev = i*(abs(pos[i] - pos[i-1]))+ prev
        return ans % (10**9 + 7)
            
        
        
            
            
                
        