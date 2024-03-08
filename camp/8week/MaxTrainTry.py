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
        graph = defaultdict(list)

        for start, end in train:
            graph[start].append(end)
            graph[end].append(start)

        queue = deque([[1, passenger[0]]])

        while queue:
            cur_v, cur_cost = queue.popleft()

            if answer[-1] < cur_cost or (answer[-1] == cur_cost and answer[0] < cur_v):
                answer = [cur_v, cur_cost]

            for next_v in list(graph[cur_v]):
                next_cost = cur_cost + passenger[next_v - 1]
                graph[cur_v].remove(next_v)
                graph[next_v].remove(cur_v)
                queue.append([next_v, next_cost])


        return answer


print(Solution.soulution(Solution, n=5, passenger=[1,1,2,3,4], train=[[1,2],[1,3],[1,4],[1,5]]))
