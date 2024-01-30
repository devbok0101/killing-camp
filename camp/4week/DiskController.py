import heapq


class Solution:

    def solution(jobs):
        answer = 0

        # 작업이 요청되는 시점이 빠른 순으로 정렬한다.
        # 하드디스크가 작업을 수행하고 있지 않을 때에는 먼저 요청이 들어온 작업부터 처리합니다.
        # 해당 제약 조건 때문에 sort를 하면 안된다고 잘못 생각한 점
        # [[2, 3], [0, 9], [2, 6]] 이럴 경우, 0번 인덱스가 중요한게 아니라, 요청시점이 작은것을 시작으로 하는것이 중요했다.
        jobs.sort()

        # 작업을 관리할 heap 초기화
        heap = []

        # 현재 시간, 완료 작업 수, 총 대기 시간
        current_time, completed_jobs, total_response_time = 0, 0, 0
        jobs_idx = 0  # 현재 처리중인 index

        # 모든 작업이 완료 될 때까지 반복
        while completed_jobs < len(jobs):
            # 현재 시간에서 처리 가능한 작업을 우선 순위 큐에 넣기
            while jobs_idx < len(jobs) and jobs[jobs_idx][0] <= current_time:
                start, duration = jobs[jobs_idx]
                heapq.heappush(heap, (duration, start))
                jobs_idx += 1

            if heap:
                # 우선순위큐에 데이터가 있으면, 데이터를 뽑는데, 그 데이터는 소요시간이 가장 적은 작업이다.
                duration, start = heapq.heappop(heap)
                # 아래 로직은 걸린시간과 현재 시간 업데이트
                current_time += duration
                total_response_time += current_time - start
                completed_jobs += 1
            else:
                # 처리할 작업이 없으면 현재 시간 증가
                # 가장 첫번째 소요 작업이 항상 0일 경우는 없으므로
                current_time = jobs[jobs_idx][0]

        return total_response_time // len(jobs)


print(Solution.solution(jobs=[[2, 3], [3, 5], [4, 2]]))
