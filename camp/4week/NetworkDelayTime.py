import heapq
import sys
from collections import defaultdict
from typing import List


class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:

        def dijkstra(graph):
            # 1부터 n까지 n개의 노드 cost 적어두기
            costs = [sys.maxsize for _ in range(n + 1)]
            pq = [(0, k)]
            costs[k] = 0

            while pq:
                cur_cost, cur_v = heapq.heappop(pq)
                for cost, next_v in graph[cur_v]:
                    next_cost = cur_cost + cost
                    if next_cost < costs[next_v]:
                        costs[next_v] = next_cost
                        heapq.heappush(pq, (next_cost, next_v))

            # 0번째를 제외한 나머지 담아 주기 왜?
            # index 0번째에는 sys.maxsize값이 무조건 들어 있음, 그것을 제외한 다시 담아주기

            new_costs = costs[1:]

            for cost in new_costs:
                if cost == sys.maxsize:
                    return -1
            return max(new_costs)

        graph = defaultdict(list)
        for source, target, weight in times:
            graph[source].append((weight, target))

        return dijkstra(graph)

print(Solution.networkDelayTime(Solution, times=[[1,2,1],[2,1,3]], n=2, k=2))
