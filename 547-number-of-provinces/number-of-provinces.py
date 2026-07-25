from collections import deque
class Solution:
    def findCircleNum(self, grid: List[List[int]]) -> int:
        # m = len(grid)
        # n = len(grid[0])

        # vis = [[0 for _ in range(n)]for _ in range(m)]

        # d = {
        #     (1,0),
        #     (0,1),
        #     (-1,0),
        #     (0,-1)
        # }

        # q = deque()
        # count = 0

        # for i in range(m):
        #     for j in range(n):
        #         if vis[i][j]==0 and grid[i][j]==1:
        #             count+=1
        #             q.append((i,j))
        #             vis[i][j]=1
        #             while q:
        #                 u,v = q.popleft()
        #                 for x,y in d:
        #                     xu = x+u
        #                     yv = y+v

        #                     if 0<=xu<m and 0<=yv<n and vis[xu][yv]==0 and grid[xu][yv]==1:
        #                         q.append((xu,yv))
        #                         vis[xu][yv]=1
        # return count

        vis = [False]*len(grid)
        n = len(grid)
        count = 0
        q = deque()

        for i in range(len(vis)):
            if not vis[i]:
                count+=1
                vis[i]=True
                q.append(i)
                while q:
                    city = q.popleft()
                    for nei in range(len(grid[city])):
                        if grid[city][nei]==1  and not vis[nei]:
                            vis[nei]=True
                            q.append(nei) 
        return count



        
        