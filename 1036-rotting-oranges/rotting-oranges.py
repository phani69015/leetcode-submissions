from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()
        mins = 0
        fresh = 0
        m = len(grid)
        n = len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j]==2:
                    q.append((i,j))
                elif grid[i][j]==1:
                    fresh+=1
        d = {
            (0,1),
            (1,0),
            (-1,0),
            (0,-1)
        }
        while q:
            level = len(q)
            for _ in range(level):
                x,y = q.popleft()
                for i,j in d:
                    xi = x+i
                    yj = y+j
                    if 0<=xi<m and 0<=yj<n and grid[xi][yj]==1:
                        grid[xi][yj] = 2
                        fresh -= 1
                        q.append((xi,yj))
            if q:
                mins+=1
        
        return mins if fresh ==0 else -1



        