class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        res = []
        for i in range(len(score)):
            heappush(res , (-score[i],i))
        ans = [''] * len(score)
        r = 1
        rank = ["Gold Medal", "Silver Medal", "Bronze Medal"]
        while len(res) != 0:
            _ , i = heappop(res)
            if r <= 3:
                ans[i] = rank[r-1]
            else:
                ans[i] = f'{r}'
            r += 1
        return ans

        