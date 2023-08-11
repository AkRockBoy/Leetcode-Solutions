#User function Template for python3

class Solution:
    
    def count(self, nums , n , target):

        dp = [[0 for i in range(target+1)] for j in range(n+1)]

        for i in range(target+1):
            if i % coins[0] == 0:
                dp[0][i] = 1

        for ind in range(1 , n ):
            for cur_amount in range(target + 1):
    
                not_take = dp[ind-1][cur_amount]

                take = 0
                if cur_amount >= coins[ind]:
                    take = dp[ind][cur_amount - coins[ind]]
                
                dp[ind][cur_amount] = take + not_take
        
        return dp[n-1][target]

        '''
        nums.sort()
        memo = {}
        def fun(i , target):
            if i == n or target < 0:
                return 0
                
            if (i , target) in memo:
                return memo[(i , target)]
                
            if target == 0:
                 return 1
                 
            if nums[i] > target:
                memo[(i , target)] = fun(i+1 , target)
            else:
                memo[(i , target)] = fun(i , target-nums[i]) + fun(i + 1 , target)
            return memo[(i , target)]
                
        return fun(0 , target)
        '''
        

        
    
        # code here 



#{ 
 # Driver Code Starts
#Initial Template for Python 3

import sys
sys.setrecursionlimit(10**6)

if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        sum,N = list(map(int, input().strip().split()))
        coins = list(map(int, input().strip().split()))
        ob = Solution()
        print(ob.count(coins,N,sum))

# } Driver Code Ends