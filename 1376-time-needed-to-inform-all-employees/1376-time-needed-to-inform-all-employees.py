class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:

        so = defaultdict(list)
        for i in range(len(manager)):
            so[manager[i]].append(i)
        
        def dfs(root):
            ans = 0
            for v in so[root]:
                ans = max(dfs(v) + informTime[root], ans)
            return ans
        
        return dfs(headID)
    