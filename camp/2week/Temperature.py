from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        answer = [0 for _ in range(len(temperatures))]
        stack = []

        for cur_day, cur_temperature in enumerate(temperatures):
            while stack and cur_temperature > stack[-1][1]:
                before_day = stack.pop()[0]
                answer[before_day] = cur_day - before_day
            stack.append((cur_day, cur_temperature))

        return answer


print(Solution.dailyTemperatures(Solution, temperatures=[73,74,75,71,69,72,76,73]))