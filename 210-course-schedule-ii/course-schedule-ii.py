class Solution:
    def findOrder(self, n: int, grid: List[List[int]]) -> List[int]:

        indegree = [0]*n
        adj = [[] for _ in range(n)]

        for i,j in grid:
            adj[j].append(i)

        for i in range(n):
            for nei in adj[i]:
                indegree[nei]+=1
        q = deque()
        for i in range(n):
            if indegree[i]==0:
                q.append(i)  

        ans = []

        while q:
            key = q.popleft()
            ans.append(key)

            for nei in adj[key]:
                indegree[nei]-=1
                if indegree[nei]==0:
                    q.append(nei)

        return ans if len(ans)==n else []     