from collections import deque
from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        row = len(grid)
        col = len(grid[0])
        visited = [[False] * row for _ in range(col)]
        answer = 0
        dx = [0, -1, 0, 1]
        dy = [-1, 0, 1, 0]

        def bfs(i, j):
            visited[i][j] = True
            queue = deque()
            queue.append((i, j))

            while queue:
                cur_x, cur_y = queue.popleft()
                for i in range(4):
                    next_x = cur_x + dx[i]
                    next_y = cur_y + dy[i]

                    if 0 <= next_x < row and 0 <= next_y < col and grid[next_x][next_y] == "1" and not visited[next_x][next_y]:
                        visited[next_x][next_y] = True
                        queue.append((next_x, next_y))

        for i in range(row):
            for j in range(col):
                if grid[i][j] == "1" and not visited[i][j]:
                    bfs(i, j)
                    answer += 1

        return answer



print(Solution.numIslands(Solution, grid=[["1","1","1","1","0"],
                                          ["1","1","0","1","0"],
                                          ["1","1","0","0","0"],
                                          ["0","0","0","0","0"]]))
