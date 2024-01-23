from collections import deque
from copy import deepcopy


class Solution:
    def solution(self, lab: list[list[int]]) -> int:

        row = len(lab)
        column = len(lab[0])

        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]

        def set_wall(count, answer):
            if count == 3:
                return bfs(answer)
            for cur_row in range(row):
                for cur_column in range(column):
                    if lab[cur_row][cur_column] == 0:
                        lab[cur_row][cur_column] = 1
                        answer = set_wall(count + 1, answer)
                        lab[cur_row][cur_column] = 0
            return answer

        def bfs(answer):
            virus_lab = deepcopy(lab)
            queue = deque()
            for cur_row in range(row):
                for cur_column in range(column):
                    if virus_lab[cur_row][cur_column] == 2:
                        queue.append((cur_row, cur_column))

            while queue:
                origin_virus_row, origin_virus_column = queue.popleft()
                for index in range(4):
                    next_row = origin_virus_row + dx[index]
                    next_column = origin_virus_column + dy[index]

                    if 0 <= next_row < row and 0 <= next_column < column and virus_lab[next_row][next_column] == 0:
                        virus_lab[next_row][next_column] = 2
                        queue.append((next_row, next_column))

            count = 0
            for cur_row in range(row):
                for cur_column in range(column):
                    if virus_lab[cur_row][cur_column] == 0:
                        count += 1
            return max(answer, count)

        answer = 0
        return set_wall(0, answer)



print(Solution.solution(Solution, lab=[[0, 0, 0, 0, 0, 0],
                                       [1, 0, 0, 0, 0, 2],
                                       [1, 1, 1, 0, 0, 2],
                                       [0, 0, 0, 0, 0, 2]]))
