from collections import deque
class Solution:
    def countConnected(self, V, edges):
        # code here 
        
        q = deque()
        
        adj = [[]for _ in range(V)]
        for x,y in edges:
            adj[x].append(y)
            adj[y].append(x)
            
        vis = [False]*V
        count = 0
        
        for i in range(V):
            comp = []
            if not vis[i]:
                q.append(i)
                vis[i]=True
                
                while q:
                    key = q.popleft()
                    for nei in adj[key]:
                        if not vis[nei]:
                            vis[nei]=True
                            q.append(nei)
                count+=1
        return count
        