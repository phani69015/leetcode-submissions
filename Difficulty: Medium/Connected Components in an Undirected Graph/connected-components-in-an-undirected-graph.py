from collections import deque
class Solution:
    def getComponents(self, V, edges):
        # code here
        # code here
        q = deque()
        
        adj = [[]for _ in range(V)]
        for x,y in edges:
            adj[x].append(y)
            adj[y].append(x)
            
        vis = [False]*V
        res = []
        
        for i in range(V):
            comp = []
            if not vis[i]:
                q.append(i)
                vis[i]=True
                
                while q:
                    key = q.popleft()
                    comp.append(key)
                    
                    for nei in adj[key]:
                        if not vis[nei]:
                            vis[nei]=True
                            q.append(nei)
                res.append(comp)
        return res
            