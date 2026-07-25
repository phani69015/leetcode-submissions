class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])

        vis = [[0 for i in range(n)]for _ in range(m)]

        d = {
            (1,0),
            (0,1),
            (-1,0),
            (0,-1)
        }

        q = deque()
        count = 0

        for i in range(m):
            for j in range(n):
                if vis[i][j]==0 and grid[i][j]=='1':
                    count+=1
                    q.append((i,j))
                    vis[i][j]=1
                    while q:
                        u,v = q.popleft()
                        for x,y in d:
                            ux = u+x
                            vy = v+y
                            if 0<=ux<m and 0<=vy<n and grid[ux][vy]=='1' and vis[ux][vy]==0:
                                q.append((ux,vy))
                                vis[ux][vy]=1
        return count









        