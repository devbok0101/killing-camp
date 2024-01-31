
import sys
import heapq


class Solution:
    def smallestRange(self, nums):
        # nums[idx]의 값들이 어떤 리스트에 속해 있는지 표시 남기기
        # [4,10,15,24,26] -> [[4,0],[10,0],[15,0],[24,0],[26,0]]
        for i in range(len(nums)):
            nums[i] = [[val, i] for val in nums[i]]
        # 힙 자료구조를 위한 초기화
        pq = []
        # 최대값 계산?
        max_val = -sys.maxsize


        for i in range(len(nums)):
            # 각 리스트의 첫번째 원소를 우선순위 큐에 넣어주기
            heapq.heappush(pq, nums[i][0])
            # 그러면서, 첫번째 원소들 중에서 최댓값 구하기
            max_val = max(max_val, nums[i][0][0])
        # 우선순위로 얻는 최솟값과 최댓값으로 범위 최초 설정하기
        answer = [pq[0][0], max_val]
        # 이녀석의 역할은 무엇인가?
        index_list = [0] * len(nums)

        # 최소범위 구하는 로직
        while True:
            min_val, idx = heapq.heappop(pq)
            # 최소값을 뽑아냈으므로, 해당 배열의 다음 원소로 넘어가기 위한 로직
            index_list[idx] += 1

            # 다음 원소로 넘어가다가, 마지막 값에 도달하면 종료하는 조건
            if index_list[idx] == len(nums[idx]):
                break
            # 다음 원소 값, 원소가 속한 배열 번호 구하기
            next_num = nums[idx][index_list[idx]]
            heapq.heappush(pq, next_num)
            # 최댓값 갱신
            max_val = max(max_val, next_num[0])

            # 우선순위큐로 얻은 최솟값과 최댓값 비교한 값 vs 현재 저장된 answer의 최솟 최댓 값 범위 비교하기
            if max_val - pq[0][0] < answer[1] - answer[0]:
                answer = [pq[0][0], max_val]

        return answer

print(Solution.smallestRange(Solution, nums=[[4,10,15,24,26],[0,9,12,20],[5,18,22,30]]))