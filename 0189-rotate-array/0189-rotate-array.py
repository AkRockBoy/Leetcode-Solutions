class Solution:
    def rotate(self, l: List[int], k: int) -> None:
        n=len(l)
        k=k % n
        l[:]=l[n-k:]+l[:n-k]
        