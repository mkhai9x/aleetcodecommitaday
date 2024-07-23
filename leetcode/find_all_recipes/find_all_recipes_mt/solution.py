from collections import defaultdict, deque
from typing import List

'''
Input: recipes = ["bread","sandwich"], ingredients = [["yeast","flour"],["bread","meat"]], supplies = ["yeast","flour","meat"]
Output: ["bread","sandwich"]
Explanation:
We can create "bread" since we have the ingredients "yeast" and "flour".
We can create "sandwich" since we have the ingredient "meat" and can create the ingredient "bread".


Input: recipes = ["bread","sandwich","burger"], ingredients = [["yeast","flour"],["bread","meat"],["sandwich","meat","bread"]], supplies = ["yeast","flour","meat"]
Output: ["bread","sandwich","burger"]
Explanation:
We can create "bread" since we have the ingredients "yeast" and "flour".
We can create "sandwich" since we have the ingredient "meat" and can create the ingredient "bread".
We can create "burger" since we have the ingredient "meat" and can create the ingredients "bread" and "sandwich".
 
'''

class Solution:
  def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
    graph = defaultdict(list)
    in_degree = defaultdict(int)

    # construct the graph

    for i, recipe in enumerate(recipes):
      for ingredient in ingredients[i]:
        graph[ingredient].append(recipe)
        in_degree[recipe] += 1

    queue = deque(supplies) # the queue only contain all the supplies level items
    result = []
    while queue:
      current = queue.popleft()
      if current in in_degree:
        result.append(current)

      for neighbor in graph[current]:
        in_degree[neighbor] -= 1
        if in_degree[neighbor] == 0:
          queue.append(neighbor)

    return result