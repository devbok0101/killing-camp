from collections import deque
from typing import List


class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:

        def bfs(graph, start_v):
            q = deque()
            q.append(start_v)
            visited = {start_v: True}

            while q:
                cur_v = q.popleft()
                for next_v in graph[cur_v]:
                    if next_v not in visited:
                        q.append(next_v)
                        visited[next_v] = True

        bfs(graph, 0)

        return True


print(Solution.isBipartite(Solution, graph=[[1, 2, 3], [0, 2], [0, 1, 3], [0, 2]]))
