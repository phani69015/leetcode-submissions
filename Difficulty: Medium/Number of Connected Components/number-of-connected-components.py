from collections import deque
class Solution:
    def countConnected(self, V, edges):
        # code here
        q = deque()
        
        adj = [[]for _ in range(V)]
        for x,y in edges:
            adj[x].append(y)
            adj[y].append(x)
            
        vis = [0]*V
        vis[0]=1
        q.append(0)
        count =0
        while q:
            key = q.popleft()
            for nei in adj[key]:
                if vis[nei]!=1:
                    vis[nei]=1
                    q.append(nei)
            if not q:
                count +=1
                for i in range(len(vis)):
                    if vis[i]==0:
                        q.append(i)
                        vis[i]+=1
                        break
        return count
            
        