from collections import deque
from typing import List


class Solution:
    def canVisitAllRooms(self, rooms: list[list[int]]) -> bool:
        visited = [False for _ in range(len(rooms))]

        def bfs(cur):
            visited[cur] = True
            queue = deque([cur])

            while queue:
                cur_v = queue.popleft()
                for next_v in rooms[cur_v]:
                    if not visited[next_v]:
                        visited[next_v] = True
                        queue.append(next_v)

        bfs(0)

        return all(visited)

print(Solution.canVisitAllRooms(Solution, rooms=[[1,3],[3,0,1],[2],[0]]))