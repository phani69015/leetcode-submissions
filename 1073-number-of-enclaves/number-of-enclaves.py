from collections import deque
class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        q = deque()

        for i in range(m):
            for j in range(n):
                if i == 0 or i == m-1 or j == 0 or j == n-1:                    
                    if grid[i][j]==1:
                        q.append((i,j))
                        grid[i][j]=0

        d = {
            (0,1),
            (1,0),
            (-1,0),
            (0,-1)
        }

        while q:
            x,y = q.popleft()
            for i,j in d:
                xi = x+i
                yj = y+j

                if 0<=xi<m and 0<=yj<n:
                    if grid[xi][yj]==1:
                        grid[xi][yj]=0 
                        q.append((xi,yj))
        c = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j]==1:
                    c+=1
        return c


        