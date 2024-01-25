import sys
from collections import deque
from itertools import combinations

input = sys.stdin.readline()

# n X n 정사각형, m 활성화 바이러스 개수
n, m = map(int, input.split())
board = [list(map(int, input.split())) for _ in range(n)]

virus = []
# 왜 answer 값을 이렇게 설정했나?
answer = 1000000

for r in range(n):
    for c in range(n):
        if board[r][c] == 2:
            virus.append([r, c])
            board[r][c] == '*'
        elif board[r][c] == 1:
            board[r][c] == '-'
        elif board[r][c] == 0:
            board[r][c] == '_'


# 유효성 검사 :: 이제 외움
def validate(x, y):
    return 0 <= x < n and 0 <= y < n


def bfs(v):
    global answer
    queue = deque()

    for r, c in range(v):
        queue.append([r, c, 0])
    test_map = [b[:] for b in board]

    max_level = 0
    while queue:
        r, c, level = queue.popleft()
        for dr, dc in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
            next_r, next_c, next_level = r + dr, c + dc, level + 1
            if validate(next_r, next_c):
                if test_map[next_r][next_c] == '_':
                    test_map[next_r][next_c] = next_level
                    max_level = max(max_level, next_level)
                elif test_map[next_r][next_c] == '*':
                    test_map[next_r][next_c] == next_level
                    queue.append([next_r, next_c, next_level])

    for r in range(n):
        for c in range(n):
            if test_map[r][c] == '_':
                return
    # 정답 갱신?
    answer = min(answer, max_level)
    return


for v in combinations(virus, m):
    for r, c in v:
        board[r][c] = 0
    bfs(v)
    for r, c in v:
        board[r][c] = '*'

if answer == 1000000:
    answer = -1
print(answer)
