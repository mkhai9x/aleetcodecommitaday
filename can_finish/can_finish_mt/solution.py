from collections import deque, defaultdict
from types import List

'''
Input: numCourses = 2, prerequisites = [[1,0]]
Output: true
Explanation: There are a total of 2 courses to take. 
To take course 1 you should have finished course 0. So it is possible.

'''


class Solution:
  def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
    graph = defaultdict(list)
    in_degree = defaultdict(int)

    for each in prerequisites:
      graph[each[1]].append(each[0])
      in_degree[each[0]] += 1
    
    # find all courses that does not need prerequisities
    # It means find all courses that does not in_degree i.e in_degree[course]=0
    # we will use a queue to represent it 
    queue = deque([course for course in range(numCourses) if course not in in_degree])

    result = []

    while queue:
      course_with_no_prerequisite = queue.popleft()
      if course_with_no_prerequisite in in_degree:
        result.append(course_with_no_prerequisite)

      for next_course in graph[course_with_no_prerequisite]:
        in_degree[next_course] -= 1
        if in_degree[next_course] == 0: # it mean the next_course can be finished
          queue.append(next_course)


    return len(result) == len(in_degree)