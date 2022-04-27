# https://leetcode.com/problems/find-all-possible-recipes-from-given-supplies/

class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        
        graph = defaultdict(set)
        dependency = defaultdict(int)
        i = 0
        while i < len(ingredients):
            for ingredient in ingredients[i]:
                graph[ingredient].add(recipes[i])
                dependency[recipes[i]] += 1
            i += 1
        answer = []
        queue = deque(supplies)
        while queue:
            cur = queue.popleft()
            for ing in graph[cur]:
                dependency[ing] -= 1
                if dependency[ing] == 0:
                    answer.append(ing)
                    queue.append(ing)
                    
        return answer  

# time and space complexity
# n = recipes.length
# m = ingredients[i].length
# time complexity = O(nm)
# space complexity = O(n**2)
        
        
