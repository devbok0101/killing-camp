from collections import defaultdict
from typing import List

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        top = len(cost)
        memo = {}

        def step(n):
            if n == 0 or n == 1:
                return 0
            if n not in memo:
                memo[n] = min(step(n - 1) + cost[n - 1], step(n - 2) + cost[n - 2])
            return memo[n]

        return step(top)


print(Solution.minCostClimbingStairs(Solution, cost=[0,1,2,2]))