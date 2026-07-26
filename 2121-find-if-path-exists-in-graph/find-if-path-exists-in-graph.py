from collections import deque
class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        if not edges:
            return True

        adj = [[]for _ in range(n)]
        for x,y in edges:
            adj[x].append(y)
            adj[y].append(x)

        vis = [False for _ in range(n)]
        count = 0
        q = deque()
        q.append(source)
        vis[source]=True

        while q:
            key = q.popleft()
            for nei in adj[key]:
                if nei==destination:
                    return True
                if not vis[nei]:
                    vis[nei]=True
                    q.append(nei)
        return False



        
