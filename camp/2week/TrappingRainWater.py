from collections import deque
from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        answer = 0
        stack = []
        calculated_height = height[:]

        for index, cur_height in enumerate(calculated_height):
            while stack and cur_height >= stack[-1][1]:
                before_index, before_height = stack.pop()
                # stack이 있다는 것은 오른쪽 값이 크다
                if stack:
                    # 기준이 되는 height
                    standard_height = stack[-1]
                    # 물이 차는 부분 채워주기
                    for water_filling_index in range(standard_height[0] + 1, index):
                        calculated_height[water_filling_index] = cur_height
                # stack이 없다는 것은 왼쪽 값이 크다
                else:
                    # 기준이 되는 height
                    standard_height = (before_index, before_height)
                    # 물이 차는 부분 채워주기
                    for water_filling_index in range(standard_height[0] + 1, index):
                        calculated_height[water_filling_index] = before_height
            stack.append((index, cur_height))

        for index, cur_height in enumerate(calculated_height):
            answer += calculated_height[index] - height[index]

        return answer


print(Solution.trap(Solution, height=[4,2,0,3,2,5]))
