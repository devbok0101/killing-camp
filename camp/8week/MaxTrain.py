from collections import defaultdict, Counter, deque
from typing import List


class Solution:
    def soulution(self, n: int, passenger: List[int], train: list[list[int]]) -> List[int]:
        #✅ 주어진 train정보를 통해 그래프를 생성한다.
        #✅ bfs를 진행할 큐를 선언하고 1번 노드를 입력한다.
        #✅ bfs를 진행한다.
        #✅ 현재 경로의 합이 최대가 되는 경우 answer를 갱신한다.
        #✅ 자식 노드들을 큐에 입력한다.
        answer = [0,0]
        graph = defaultdict(set)
        for start, end in train:
            graph[start].add(end)
            graph[end].add(start)
        queue = deque([[1, passenger[0]]])

        while queue:
            cur_v, cur_cost = queue.popleft()

            if cur_cost > answer[1] or (cur_cost == answer[1] and cur_v > answer[0]):
                answer = [cur_v, cur_cost]

            for next_v in list(graph[cur_v]):
                next_cost = cur_cost + passenger[next_v - 1]
                graph[cur_v].remove(next_v)
                graph[next_v].remove(cur_v)
                queue.append([next_v, next_cost])

        return answer


print(Solution.soulution(Solution, n=6, passenger=[1, 1, 1, 1, 1, 1], train=[[1, 2], [1, 3], [1, 4], [3, 5], [3, 6]]))
