from collections import deque
from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        def topological_sort(numCourses, prerequisites):
            visited = []
            graph = [[] for _ in range(numCourses)]
            indegree = [0] * numCourses

            #prerequisites의 원소는 u -> v 방향을 가지는 edge를 의미함.
            # vertax : [연결된 vertax, ...]로 구성된 graph
            for v, u in prerequisites:
                graph[u].append(v)
                # indegree 기록하기
                # indegree는 해당 vertax와 연결된 개수를 의미함
                indegree[v] += 1

            # 위상정렬 수행하기
            # indegree == 0 인 정점부터 탐색 시작
            # indegree가 0이면 현재 정점인것을 의미함, 시작점이라고 볼 수 있음
            queue = deque()
            for v in range(numCourses):
                if indegree[v] == 0:
                    queue.append(v)

            while queue:
                cur_v = queue.popleft()
                visited.append(cur_v)

                # 해당 정점과 연결된 노드들의 진입차수에서 1빼기
                # 진입차수가 0인 애들이 visited로 제거 되니, 변경 된 위치를 반영하기 위해 진입차수를 빼주는 것
                for next_v in graph[cur_v]:
                    indegree[next_v] -= 1

                    # 진입차수가 0이면 방문해도 된다는 뜻이니까 queue에 추가
                    # 0이되었다는 것은 정점이므로, 빠져도됨
                    if indegree[next_v] == 0:
                        queue.append(next_v)

            # 들어야하는 강의 수 와 연결되어 제거된 개수가 같으면 모두 들은 것으로 판다
            return len(visited) == numCourses

        return topological_sort(numCourses, prerequisites)

#print(Solution.canFinish(Solution, numCourses=20, prerequisites=[[0,10],[3,18],[5,5],[6,11],[11,14],[13,1],[15,1],[17,4]]))
print(Solution.canFinish(Solution, numCourses=6, prerequisites=[[2,0], [3, 0], [3, 1], [4, 1], [3, 2], [5, 2], [5, 3], [5, 4]]))

