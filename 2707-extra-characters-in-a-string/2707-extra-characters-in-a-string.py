class Solution:
    def minExtraChar(self, s: str, s1: List[str]) -> int:
        def fun(index , s , s1 , dp):
            if index == len(s):return 0

            if dp[index] != -1: return dp[index]

            res = float('inf')
            for j in range(index , len(s)):
                s2 = s[index:j+1]
                if s2 in s1:
                    res = min(res , 0 + fun(j+1 , s , s1 , dp))
                else:
                    res = min(res , j - index + 1 + fun(j+1 , s , s1 , dp))
            dp[index] = res
            return res
        
        dp = [-1] * (len(s)+1)
        s1 = set(s1)
        return fun(0 , s , s1 , dp)
