from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans = [0] * len(temperatures)
        stack = []

        for cur_day, cur_temp in enumerate(temperatures):
            while stack and cur_temp > stack[-1][1]:
                prev_day, _ = stack.pop()
                ans[prev_day] = cur_day - prev_day
            stack.append((cur_day, cur_temp))

        return ans


print(Solution.dailyTemperatures(Solution, [30,60,90]))

# not stack == 스택이 비어있으면 true
