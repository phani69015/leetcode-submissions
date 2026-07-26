class Solution:
    def dfs(self, adj):
        # V = len(adj)
        # visited = [False] * V
        # result = []

        # for i in range(V):
        #     if not visited[i]:
        #         stack = [i]
        #         visited[i] = True

        #         while stack:
        #             node = stack.pop()
        #             result.append(node)

        #             # reverse to maintain DFS order
        #             for nei in reversed(adj[node]):
        #                 if not visited[nei]:
        #                     visited[nei] = True
        #                     stack.append(nei)

        # return result
        
        res = []
        V = len(adj)
        visited = [False] * V
        
        def dfs(node):
            visited[node]=True
            res.append(node)
            
            for nei in adj[node]:
                if not visited[nei]:
                    dfs(nei)
                    
        dfs(0)
        return res
            
            