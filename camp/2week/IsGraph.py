from collections import deque
from typing import List


class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        color = [-1 for _ in range(len(graph))]
        for index, color in enumerate(color):
            queue = deque([index])
            color[index] = 0

            while queue:
                cur_v = queue.popleft()
                for next_v in graph[cur_v]:
                    if color[next_v] -1:
                        color[next_v] = color[cur_v] ^ 1
                        queue.append(next_v)
                    elif color[next_v] == color[cur_v]:
                        return False
        return True


print(Solution.isBipartite(Solution, graph=[[1, 2, 3], [0, 2], [0, 1, 3], [0, 2]]))
