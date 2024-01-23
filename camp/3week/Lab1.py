import sys
from collections import deque, Counter
from itertools import combinations

input = sys.stdin.readline

# 콘솔에서 입력 받은 값 담아주기
n, m = map(int, input().split())
# map에 담은 값을 list로 변환하고, for문을 돌려 2차원 배열로 담기
board = [list(map(int, input().split())) for _ in range(n)]

virus, empty = [], []
answer = 0

# 빈칸과 바이러스의 위치를 리스트에 담아준다.
for row in range(n):
    for col in range(m):
        if board[row][col] == 2:
            virus.append([row, col])
        elif board[row][col] == 0:
            empty.append([row, col])

# 유효 범위 :: 해당 부분은 매우 익숙
def in_range(n_row, n_col):
    return 0 <= n_row < n and 0 <= n_col < m

# 좀 더 쉬운 BFS 부터 이해해보자
def bfs():
    global answer
    tmp_board = [b[:] for b in board]
    queue = deque(virus)

    while queue:
        c_row, c_col = queue.popleft()
        for dr, dc in [[-1, 0], [1, 0], [0, -1] , [0, 1]]:
            n_row, n_col = c_row + dr, c_col + dc
            if in_range(n_row, n_col) and tmp_board[n_row][n_col] == 0:
                tmp_board[n_row][n_col] = 2
                queue.append((n_row, n_col))
    ## 엄청 좋은 내장 모듈 Counter 리스트 내 각 요소의 개수를 알 수 있음
    count = Counter([])
    for row in tmp_board:
        count += Counter(row)
    # 가장 큰 안전 영역 구하기
    answer = max(answer, count[0])
    return

# 새로운 벽 3개를 설치하는 경우의 수(empty에 빈 칸을 저장한 이유)
# -> 빈칸에 벽을 3개 세워야하기 때문에, 빈칸의 위치를 알아야 할 필요가 있음
for new_wall in combinations(empty, 3):
    row, col = [], []
    for r , c in new_wall:
        row.append(r)
        col.append(c)
        if board[r][c] != 0:
            break
    else:
        for i in range(3):
            # 실제 board에 벽을 세우는 작업
            board[row[i]][col[i]] = 1
        bfs()
        for i in range(3):
            # 다시 board를 원상 복귀 시키는 작업
            board[row[i]][col[i]] = 0

print(answer)

