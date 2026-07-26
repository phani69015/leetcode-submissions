from collections import deque
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        d = {
            (0,1),
            (1,0),
            (-1,0),
            (0,-1)
        }

        q = deque()

        m = len(grid)
        n = len(grid[0])
        lens = 0

        for i in range(m):
            for j in range(n):
                temp = 0
                if grid[i][j]==1:
                    q.append((i,j))
                    grid[i][j]=0
                    temp+=1
                    while q:
                        u,v = q.popleft()
                        for x,y in d:
                            ux = u+x
                            vy = v+y
                            if 0<=ux<m and 0<=vy<n and grid[ux][vy]==1:
                                grid[ux][vy]=0
                                q.append((ux,vy))
                                temp+=1

                lens=max(lens,temp)
        return lens





        