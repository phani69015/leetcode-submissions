from collections import deque
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        if image[sr][sc]==color:
            return image
        rows = len(image)
        cols = len(image[0])

        q = deque()
        q.append((sr,sc))
        curr = image[sr][sc]
        image[sr][sc]=color

        d = {
            (0,1),
            (1,0),
            (0,-1),
            (-1,0)
        }

        while q:
            i,j = q.popleft()
            for x,y in d:
                xi = x + i
                yj = y + j

                if 0<=xi<rows and 0<=yj<cols and image[xi][yj]==curr:
                    image[xi][yj]=color
                    q.append((xi,yj))

        return image





        







        

        
        