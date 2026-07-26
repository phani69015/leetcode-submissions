from collections import deque
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        m = len(board)
        n = len(board[0])
        q = deque()

        v = [[False for _ in range(n)]for _ in range(m)]

        for i in range(m):
            for j in range(n):
                if i == 0 or i == m - 1 or j == 0 or j == n - 1:
                    if board[i][j]=="O":
                        q.append((i,j))
                        v[i][j]=True
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
                    if v[xi][yj]==False and board[xi][yj]=="O":
                        q.append((xi,yj))
                        v[xi][yj]=True


        
        for i in range(m):
            for j in range(n):
                if v[i][j]==False and board[i][j]=="O":
                    board[i][j]="X"

        
                



                