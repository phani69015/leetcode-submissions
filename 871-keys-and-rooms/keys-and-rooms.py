from collections import deque
class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:

        n = len(rooms)
        vis = [False for _ in range(n)]
        q = deque()
        q.append(0)
        vis[0]=True
        while q:
            key = q.popleft()
            for nei in rooms[key]:
                if not vis[nei]:
                    vis[nei]=True
                    q.append(nei)
        return all(vis)



        
        