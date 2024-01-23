import sys
from copy import deepcopy

input = sys.stdin.readline

lab = []
virus_position = []
n, m = map(int, input().split())

complete_count = 0

for row in range(n):
    input_one_line = list(map(int, input().split()))
    for column in range(n):
        if input_one_line[column] == 2:
            # 바이러스 위치와 확산에 걸린 시간 함께 저장 아하!
            virus_position.append([row, column, 0])
        elif input_one_line[column] == 0:
            complete_count += 1
    lab.append(input_one_line[:])

# 최종 출력 시간
min_time = int(10e9)


# 바이러스 중에서 활성화 시킬 바이러스를 고르는 dfs
def select_virus(depth, select, start):
    if depth == m:
        deffusion(deepcopy(select))
        return
    for i in range(start, len(virus_position)):
        select.append(virus_position[i])
        select_virus(depth + 1, select, i + 1)
        select.remove(virus_position[i])


dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]


def deffusion(select):
    global min_time

    max_time = 0
    virus_count = 0
    temp_lab = deepcopy(lab)

    while select:
        x, y, time = select.pop(0)
        # 활성된 바이러스는 3으로 표시
        temp_lab[x][y] = 3

        # 빈칸이 모두 채워진 경우
        if virus_count == complete_count:
            min_time = min(min_time, max_time)
            return

        if time >= min_time:
            return

        # 4방향 처리
        for index in range(4):
            next_row = x + dx[index]
            next_col = y + dy[index]

            if 0 <= next_row < n and 0 <= next_col < n:
                if temp_lab[next_row][next_col] == 0:
                    virus_count += 1
                    temp_lab[next_row][next_col] = 3
                    select.append([next_row, next_col, time + 1])
                    max_time = time + 1
                elif temp_lab[next_row][next_col] == 2:
                    temp_lab[next_row][next_col] = 3
                    select.append([next_row, next_col, time + 1])


select_virus(0, [], 0)

if min_time == int(10e9):
    print(-1)
else:
    print(min_time)
