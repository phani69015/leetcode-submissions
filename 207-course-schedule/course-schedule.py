class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        indegree = [0]*numCourses

        adj = [[] for _ in range(numCourses)]

        for i,j in prerequisites:
            adj[j].append(i)

        for i in range(numCourses):
            for nei in adj[i]:
                indegree[nei]+=1

        q = deque()

        for i in range(numCourses):
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

        return len(ans) == numCourses

        