
from collections import deque
from typing import List

class Solution:
    def findAllRecipes(
        self,
        recipes: List[str],
        ingredients: List[List[str]],
        supplies: List[str]
    ) -> List[str]:

        ind = {}
        adj = {}

        # Build graph
        for i in range(len(recipes)):
            recipe = recipes[i]
            ind[recipe] = len(ingredients[i])

            for ingredient in ingredients[i]:
                if ingredient not in adj:
                    adj[ingredient] = []

                adj[ingredient].append(recipe)

        # Initially available ingredients
        q = deque(supplies)

        ans = []

        # Topological sort
        while q:
            item = q.popleft()

            # If this item is a recipe, we successfully created it
            if item in ind:
                ans.append(item)

            # This item may help unlock some recipes
            for recipe in adj.get(item, []):
                ind[recipe] -= 1

                if ind[recipe] == 0:
                    q.append(recipe)

        return ans
