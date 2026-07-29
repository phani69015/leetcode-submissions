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
            
            