class Solution:
    def isFascinating(self, n: int) -> bool:
        s1 = str(n)
        s2 = str(n * 2)
        s3 = str(n * 3)
        concat = s1 + s2 + s3
        if '0' in concat:return False
        ans = set(concat)
        return len(ans) == len(concat) and len(concat) == 9

        