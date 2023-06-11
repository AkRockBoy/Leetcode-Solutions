class Solution:
    def smallestString(self, s: str) -> str:
        n = len(s)
        if n == 1: 
            if s == 'a':return 'z'
            else:
                return chr(ord(s)-1)
        res = list(s)
        i = 0
        while i < n and s[i] == 'a':
            i += 1
        if i < n:
            for j in range(i, n):
                if s[j] != 'a':
                    res[j] = chr(ord(s[j]) - 1)
                else:
                    break
        else:res[-1] = 'z'
        return ''.join(res)

