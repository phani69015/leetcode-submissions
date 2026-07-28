from collections import deque
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        if image[sr][sc]==color:
            return image
        rows = len(image)
        cols = len(image[0])

        #bfs
        # curr = image[sr][sc]
        # image[sr][sc]=color

        # q = deque()
        # q.append((sr,sc))

        # d = {
        #     (-1,0),
        #     (0,-1),
        #     (1,0),
        #     (0,1)
        # }

        # while q:
        #     a,b = q.popleft()
        #     for x,y in d:
        #         ax,by = a+x , b+y
        #         if 0<=ax<rows and 0<=by<cols and image[ax][by]==curr:
        #             q.append((ax,by))
        #             image[ax][by]=color 
        # return image

        #dfs 

        curr = image[sr][sc]

        def dfs(a,b):
            d = {
                (-1,0),
                (0,-1),
                (1,0),
                (0,1)
            }
            image[a][b]=color
            for x,y in d:
                ax,by = a+x , b+y
                if 0<=ax<rows and 0<=by<cols and image[ax][by]==curr:
                    dfs(ax,by)
            
        dfs(sr,sc)

        return image




            



        
            







        







        

        
        