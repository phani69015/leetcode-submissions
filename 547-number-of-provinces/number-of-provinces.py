from collections import deque
class Solution:
    def findCircleNum(self, matrix: List[List[int]]) -> int:
        #approach 1 -> convert to adjaceny list and find no of components
        # def matrix_to_list(matrix):
        #     adj_list = []
            
        #     for i in range(len(matrix)):
        #         neighbors = []
        #         for j in range(len(matrix[i])):
        #             if matrix[i][j] == 1:
        #                 neighbors.append(j)
        #         adj_list.append(neighbors)
                
        #     return adj_list

        # adj = matrix_to_list(grid)

        # v = [False for _ in range(len(adj))]
        # c = 0
        # q = deque()

        # for i in range(len(adj)):
        #     if not v[i]:
        #         c+=1
        #         q.append(i)
        #         v[i]=True

        #         while q:
        #             key = q.popleft()
        #             for nei in adj[key]:
        #                 if not v[nei]:
        #                     v[nei]=True
        #                     q.append(nei)
        # return c

        #approach 2 -> using graph dfs 
        n = len(matrix)
        v = [False]*n
        c = 0
        q = deque()

        for i in range(n):
            if not v[i]:
                c+=1
                q.append(i)
                v[i]=True
                while q:
                    key = q.popleft()
                    for nei in range(n):
                        if not v[nei] and matrix[key][nei]==1:
                            v[nei]=True
                            q.append(nei)
        

        return c





        
        