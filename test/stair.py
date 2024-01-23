from collections import deque
from typing import List


class Solution:
    def climbStairs(self, n: int) -> int:

        result = {1:1, 2:2}
        def stair(n):
            if n == 1: return 1
            if n == 2: return 2
            if n not in result:
                for i in range(3, n+1):
                    result[i] = result[i - 1] + result[i - 2]
                return result[n]

        return stair(n)


print(Solution.climbStairs(Solution, n=6))
