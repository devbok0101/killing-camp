import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
board = [input().rstrip() for _ in range(n)]
visited = set()

answer = 0
queue = deque()
for r in range(n):
    for c in range(m):
        if board[r][c] == 'R':
            rr, rc = r, c
        elif board[r][c] == 'B':
            br, bc = r, c

queue.append([rr, rc, br, bc, 1])
visited.add((rr, rc, br, bc))


def move(r, c, dr, dc):
    count = 0
    while board[r + dr][c + dc] != "#" and board[r][c] != "0":
        r += dr
        c += dc
        count += 1
    return r, c, count


while queue:

    rr, rc, br, bc, level = queue.popleft()

    if level > 10:
        break

    for dr, dc in [[-1, 0], [1, 0], [0, 1], [0, -1]]:
        n_rr, n_rc, r_count = move(rr, rc, dr, dc)
        n_br, n_bc, b_count = move(br, bc, dr, dc)

        # 파란공이 들어가 버린 경우
        if board[n_br][n_bc] == "O":
            continue

        if (n_rr, n_rc, n_br, n_bc) in visited:
            continue

        # 빨간공이 들어간 경우
        if board[n_rr][n_rc] == "O":
            answer = 1
            break
        # 두 구슬의 위치가 같은 경우 더 멀리서 이동된 구슬을 이전 칸으로 이동시켜서 수정해야함
        if n_rr == n_br and n_rc == n_bc:
            if r_count > b_count:
                n_rr -= dr
                n_rc -= dc
            else:
                n_br -= dr
                n_bc -= dc
        queue.append([n_rr, n_rc, n_br, n_bc, level + 1])
        visited.add((n_rr, n_rc, n_br, n_bc))
    else:
        continue
    break

print(answer)