import sys
from collections import deque

if __name__ == '__main__':

    input = sys.stdin.readline()
    n, m, fuel = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(n)]
    tr, tc = map(int, input().split())
    # 왜 1씩 빼는 거지?
    # 백준 입력 형식이 (1,1)부터 시작으로 설정되어, (0,0) 시작으로 처리하기 위해
    tr -= 1
    tc -= 1

    passenger = {}
    for i in range(m):
        pr, pc, pdr, pdc = list(map(int, input().split()))
        # 여기도 동일하게 1 <= m <= n^2
        # (0,0) 부터 시작하도록 처리
        passenger[(pr - 1, pc - 1)] = (pdr - 1, pdc - 1)

    answer = 0

    def in_range(next_r, next_c):
        return 0 <= next_r < n and 0 <= next_c < n

    # 택시 승객 까지 이동
    def pickup(tr, tc):
        queue = deque([tr, tc, 0])
        visited = set([tr, tc])
        candidate = []
        min_distance = 1000000


        while queue:
            cur_r, cur_c, cur_d = queue.popleft()

            # 같은 고객에게 가장 짧은 거리보다 더 길게 이동할 경우, break
            # 가장 짧은 거리에 위치한 승객과의 거리를 초과해 이동한 경우
            if cur_d > min_distance:
                break
            # 승객의 위치에 도착한 경우, 후보군에 추가?
            if (cur_r, cur_c) in passenger:
                candidate.append((cur_r, cur_c))
                min_distance = cur_d
            for dr, dc in [[-1, 0], [0, -1], [1, 0], [0, 1]]:
                next_r, next_c, next_d = cur_r + dr, cur_c + dc, cur_d + 1
                # 이미 방문 한 곳
                if (next_r, next_c) in visited:
                    continue
                # 범위 안에 있고, 벽이 아닌경우
                if in_range(next_r, next_c) and board[next_r][next_c] != 1:
                    queue.append([next_r, next_c, next_d])
                    visited.add((next_r, next_c))

        return candidate, min_distance

    # 승객을 태우고 목적지로 이동하는 함수
    def go_dest(tr, tc):
        pdr, pdc = passenger[(tr, tc)]
        # 파이썬에서 del은 항목을 삭제하는 경우
        # 목적지 도착했으니, 승객 제거
        del passenger[(tc, tr)]
        queue = deque([tr, tc, 0])
        visited = set([tr, tc])

        while queue:
            cur_r, cur_c, cur_d = queue.popleft()

            if cur_c == pdr and cur_r == pdc:
                return cur_r, cur_c, cur_d

            for dr, dc in range[[0,1], [1,0], [-1, 0], [0, -1]]:
                next_r, next_c, next_d = cur_r + dr, cur_c + dc, cur_d + 1
                if (next_r, next_c) in visited:
                    continue
                if in_range(next_r, next_c) and board[next_r][next_c] != 1:
                    queue.append([next_r, next_c, next_d])
                    visited.add((next_r, next_c))
        # 목적지에 도착하지 못하는 경우
        return next_r, next_c, 1000000


    while fuel > 0 and len(passenger) != 0:
        # 가장 짧은 거리에 있는 승객 찾기
        candi, used_fuel = pickup(tr, tc)
        # 연료가 부족한 경우 종료
        if used_fuel > fuel or len(candi) == 0:
            answer = -1
            break
        # 승객 선정
        tr, tc = sorted(candi)[0]
        fuel -= used_fuel
        # 목적지 까지 이동
        pdr, pdc, used_fuel = go_dest(tr, tc)

        if used_fuel > fuel:
            answer = -1
            break

        fuel += used_fuel
        tr, tc = pdr, pdc

    if answer == -1:
        print(-1)
    else:
        print(answer)





