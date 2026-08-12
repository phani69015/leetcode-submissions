class Solution:
    def bellmanFord(self, V: int, edges: list[list[int]], src: int) -> list[int]:
        #code here
        adj =[[] for _ in range(V)]
        
        for x,y,z in edges:
            adj[x].append([z,y])
            
        dis = [float("inf") for _ in range(V)]
        
        dis[src]=0
        
        for _ in range(V-1):
            for i in range(V):
                for wei,y in adj[i]:
                    if dis[i]+wei < dis[y]:
                        dis[y]=dis[i]+wei 
                        
        for i in range(V):
            for wei, y in adj[i]:

                if dis[i] != float("inf") and dis[i] + wei < dis[y]:
                    return [-1]
                        
        for i in range(V):
            if dis[i] == float("inf"):
                dis[i] = 100000000
        return dis
            
            