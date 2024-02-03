from collections import deque
from typing import List


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        visited = []
        graph = [[] for _ in range(numCourses)]
        indegree = [0] * numCourses

        for next, cur in prerequisites:
            graph[cur].append(next)
            indegree[next] += 1

        queue = deque()
        for vertex in range(numCourses):
            if indegree[vertex] == 0:
                queue.append(vertex)

        while queue:
            cur_v = queue.popleft()
            visited.append(cur_v)

            for next_v in graph[cur_v]:
                indegree[next_v] -= 1

                if indegree[next_v] == 0:
                    queue.append(next_v)
        if len(visited) != numCourses:
            return []
        else:
            return visited


print(Solution.findOrder(Solution, numCourses=3, prerequisites=[[1,0],[1,2],[0,1]]))
