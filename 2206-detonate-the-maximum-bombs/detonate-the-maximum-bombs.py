from typing import List

class Solution:

    def distance(self, arr1, arr2):
        ps = arr2[1] - arr1[1]
        pf = arr2[0] - arr1[0]
        return ps * ps + pf * pf

    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        m = len(bombs)
        adj = [[] for _ in range(m)]

        for i in range(m):
            for j in range(i + 1, m):
                dist = self.distance(bombs[i], bombs[j])

                if dist <= bombs[i][2] ** 2:
                    adj[i].append(j)

                if dist <= bombs[j][2] ** 2:
                    adj[j].append(i)

        def dfs(node, visited):
            visited.add(node)

            for nei in adj[node]:
                if nei not in visited:
                    dfs(nei, visited)

        ans = 0

        for i in range(m):
            visited = set()
            dfs(i, visited)
            ans = max(ans, len(visited))

        return ans