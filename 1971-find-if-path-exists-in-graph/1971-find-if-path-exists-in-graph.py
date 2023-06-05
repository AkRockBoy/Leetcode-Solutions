class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        res = defaultdict(list)
        for i , j in edges:
            res[i].append(j)
            res[j].append(i)
        visited = set()

        def dfs(s , d , visited):
            if s == d: return True
            if s not in visited:
                visited.add(s)
                for i in res[s]:
                    if(dfs(i,d,visited)):return True

        return dfs(source , destination , visited)
