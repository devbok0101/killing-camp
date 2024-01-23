from collections import deque
from typing import List


class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = [False] * len(rooms)
        # v에 연결되어 있는 곳에 방문 할거야
        def bfs(v):
            queue = deque()
            deque.append(v)
            visited[v] = True
            while queue:
                cur_v = queue.popleft()
                for next_v in rooms[cur_v]:
                    if not visited[next_v]:
                        visited[next_v] = True
                        queue.append(next_v)

        bfs(0)
        return all(visited)


print(Solution.canVisitAllRooms(Solution, rooms=[[1,3],[3,0,1],[2],[0]]))
