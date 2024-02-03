import heapq
import sys
from collections import defaultdict
from typing import List


class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int,
                       end_node: int) -> float:
        graph = defaultdict(list)
        for i, (u, v) in enumerate(edges):
            graph[u].append((v, succProb[i]))
            graph[v].append((u, succProb[i]))

        max_prob = [0.0] * n
        max_prob[start_node] = 1.0
        pq = [(-1.0, start_node)]

        while pq:
            cur_prob, cur_v = heapq.heappop(pq)
            for next_v, path_prob in graph[cur_v]:
                if -cur_prob * path_prob > max_prob[next_v]:
                    max_prob[next_v] = path_prob * -cur_prob
                    heapq.heappush(pq, (-max_prob[next_v], next_v))

        return max_prob[end_node]


print(Solution.maxProbability(Solution, n=5, edges=[[1,4],[2,4],[0,4],[0,3],[0,2],[2,3]], succProb=[0.37,0.17,0.93,0.23,0.39,0.04], start_node=3,
                              end_node=4))
