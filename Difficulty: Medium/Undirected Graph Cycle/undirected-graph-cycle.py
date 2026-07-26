from collections import deque
class Solution:
	def isCycle(self, V, edges):
		#Code here
		adj = [[] for _ in range(V)]
		
		for x,y in edges:
		    adj[x].append(y)
		    adj[y].append(x)
		    
		v = [False for _ in range(V)]
		q = deque()
		
		for i in range(V):
		    if not v[i]:
		        q.append((i,-1))
		        v[i]=True
		        
		    while q:
		        a,b = q.popleft()
		        for nei in adj[a]:
		            if not v[nei]:
    		            v[nei]=True
    		            q.append((nei,a))
                    elif nei!=b:
                        return True
        return False
		