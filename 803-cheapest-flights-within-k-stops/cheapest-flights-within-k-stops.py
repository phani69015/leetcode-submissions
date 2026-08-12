class Solution:
    def findCheapestPrice(
        self,
        V: int,
        edges: List[List[int]],
        src: int,
        dst: int,
        k: int
    ) -> int:

        adj = [[] for _ in range(V)]

        for x, y, z in edges:
            adj[x].append([z, y])

        dis = [float("inf")] * V
        dis[src] = 0

        for _ in range(k + 1):

            temp = dis.copy()

            for i in range(V):
                for wei, y in adj[i]:

                    if dis[i] != float("inf") and dis[i] + wei < temp[y]:
                        temp[y] = dis[i] + wei

            dis = temp

        if dis[dst] == float("inf"):
            return -1

        return dis[dst]