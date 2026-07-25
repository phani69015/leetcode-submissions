from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()
        fresh = 0
        mins = 0
        m = len(grid)
        n = len(grid[0])
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==2:
                    q.append((i,j))
                elif grid[i][j]==1:
                    fresh+=1
                else:
                    continue 
        dir = {
            (0,1),
            (1,0),
            (-1,0),
            (0,-1)
        }
        while q:
            level = len(q)
            for _ in range(level):
                i,j = q.popleft()
                for x,y in dir:
                    xi = i+x
                    yi = j+y
                    if 0 <= xi < m and 0<=yi<n:
                        if grid[xi][yi]==1:
                            fresh -= 1
                            grid[xi][yi] = 2
                            q.append((xi,yi)) 
            if q:
                mins += 1 
        return mins if fresh==0 else -1
        