class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])
        #bfs
        vis = [[False for _ in range(n)] for _ in range(m)]

        d = {
            (0,1),
            (0,-1),
            (1,0),
            (-1,0)
        }

        q = deque()
        c = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j]=='1' and not vis[i][j]:
                    c+=1
                    q.append((i,j))
                    vis[i][j]=True
                    while q:
                        a,b = q.popleft()
                        for x,y in d:
                            ax , by = a+x , b+y
                            if 0<=ax<m and 0<=by<n and grid[ax][by]=='1' and not vis[ax][by]:
                                q.append((ax,by))
                                vis[ax][by]=True 
        return c














        