from collections import deque
class Solution:
    
    def dfs(self,node,st,vis,adj):
        vis[node]=True
        for nei in adj[node]:
            if not vis[nei]:
                self.dfs(nei,st,vis,adj)
                
        st.append(node)
    
    
    def topoSort(self, V, edges):
        # Code here
        st = []
        vis = [False for _ in range(V)]
        
        adj = [[] for _ in range(V)]
        
        for i,j in edges:
            adj[i].append(j)
        
        for i in range(V):
            if not vis[i]:
                self.dfs(i,st,vis,adj)
                
        ans = []
        
        while st:
            ans.append(st.pop())
                
            
        return ans
    
    #kahn's algorithm or topological sort + bfs 
    
        # indegree = [0 for _ in range(V)]
    
        # adj = [[] for _ in range(V)]
        
        # for i,j in edges:
        #     adj[i].append(j)
            
        
        # for i in range(V):
        #     for node in adj[i]:
        #         indegree[node]+=1
                
        # q = deque()
                
        # for i in range(V):
        #     if indegree[i]==0:
        #         q.append(i)
                
        # ans = []
        
        # while q:
        #     key = q.popleft()
        #     ans.append(key)
            
        #     for nei in adj[key]:
        #         indegree[nei]-=1
        #         if indegree[nei]==0:
        #             q.append(nei)
                    
                
        # return ans
    
    
            
            