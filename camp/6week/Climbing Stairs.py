from collections import defaultdict
from typing import List


class Solution:
    def climbStairs(self, n: int) -> int:
        memo = [-1] * (n + 1)

        def step(n):
            if n == 1 or n == 0:
                return 1
            if memo[n] == -1:
                memo[n] = step(n - 1) + step(n - 2)
            return memo[n]

        return step(n)

print(Solution.climbStairs(Solution, n=3))