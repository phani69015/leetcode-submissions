class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        adj = {}
        ind = {}

        for i in range(len(recipes)):
            r = recipes[i]
            ind[r]=len(ingredients[i])

            for ing in ingredients[i]:
                if ing not in adj:
                    adj[ing]=[]
                adj[ing].append(r)

        q = deque(supplies)
        ans = []
        while q:
            key = q.popleft()
            if key in ind:
                ans.append(key)
            for nei in adj.get(key,[]):
                ind[nei]-=1
                if ind[nei]==0:
                    q.append(nei)
        return ans


