class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 1 or len(s) == 0 :return len(s)
        l,res=[],''
        for i in range(len(s)):
            res=s[i]
            flag=True
            for j in range(i+1,len(s)):
                if s[j] in res:
                    flag=False
                    l.append(len(res))
                    break
                else:
                    res+=s[j]
            if flag==True:
                l.append(len(res))
        return max(l)
