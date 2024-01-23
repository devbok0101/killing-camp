from collections import deque
from typing import List


class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        row = len(grid)
        visited = [[False] * row for _ in range(row)]

        if grid[0][0] == 1 or grid[row - 1][row - 1] == 1:
            return -1

        dx = [-1, -1, -1, 0, 0, 1, 1, 1]
        dy = [-1, 0, 1, -1, 1, -1, 0, 1]

        visited[0][0] = True
        queue = deque()
        queue.append((0, 0, 1))

        while queue:
            cur_x, cur_y, cur_len = queue.popleft()

            if cur_x == row - 1 and cur_y == row - 1:
                return cur_len

            for i in range(8):
                next_x, next_y = cur_x + dx[i], cur_y + dy[i]
                if 0 <= next_x < row and 0 <= next_y < row and grid[next_x][next_y] == 0 and not visited[next_x][
                    next_y]:
                    visited[next_x][next_y] = True
                    queue.append((next_x, next_y, cur_len + 1))

        return -1


print(Solution.shortestPathBinaryMatrix(Solution, grid=[[1,0,0],[1,1,0],[1,1,0]]))
