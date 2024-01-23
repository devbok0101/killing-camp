from collections import deque
from copy import deepcopy


class Solution:
    def solution(self, lab: list[list[int]], activate_virus_count: int) -> int:
        row = len(lab)
        column = len(lab[0])
        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]

        def activate_virus(answer, count):
            if count == activate_virus_count:
                return bfs(answer)

            for cur_row in range(row):
                for cur_column in range(column):
                    # 바이러스이고, 아직 활성화된 바이러스 숫자가 다 안채워졌다
                    if lab[cur_row][cur_column] == 2 and count < activate_virus_count:
                        answer = activate_virus(answer, count + 1)
                        lab[cur_row][cur_column] = 0
                    # 바이러스이고, 아직 활성화된 바이러스 숫자가 다 채워진 경우 나머지 비활성화
                    if lab[cur_row][cur_column] == 2 and count >= activate_virus_count:
                        lab[cur_row][cur_column] = "*"
            return answer

        def bfs(answer):
            virus_lab = deepcopy(lab)
            queue = deque()

            for cur_row in range(row):
                for cur_column in range(column):
                    if virus_lab[cur_row][cur_column] == 2:
                        queue.append((cur_row, cur_column))

            while queue:
                cur_row, cur_col = queue.popleft()
                for index in range(4):
                    next_row, next_column = cur_row + dx[index], cur_col + dy[index]

                    if 0 <= next_row < row and 0 <= next_column < column and virus_lab[next_row][next_column] == 0:
                        virus_lab[next_row][next_column] = index
                        queue.append((next_row, next_column))
            count = 0
            for cur_row in range(row):
                for cur_column in range(column):
                    count = max(count, virus_lab[cur_row][cur_column])
            return max(answer, count)

        count = 0
        answer = activate_virus(0, count)
        return answer


print(Solution.solution(Solution, lab=[[0, 0, 0, 0, 0, 0],
                                       [1, 0, 0, 0, 0, 2],
                                       [1, 1, 1, 0, 0, 2],
                                       [0, 0, 0, 0, 0, 2]], activate_virus_count=3))
