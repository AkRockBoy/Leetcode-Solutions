class Solution:
    def longestSemiRepetitiveSubstring(self, s: str) -> int:
        i , j = 0 , 1
        count = 0
        length = 1
        res = 1
        firstcount = 0
        while j < len(s):
            if (s[j] == s[j-1]):
                count += 1
                if count == 1:
                    firstcount = j
                if count > 1:
                    i = firstcount
                    firstcount = j
                    count += 1
                    length = j-i
            length += 1
            j += 1
            res = max(length , res)
        return res