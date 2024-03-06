from collections import Counter, defaultdict
from itertools import combinations
from typing import List


class Solution:
    def soulution(self, needs: List[List[int]], r: int) -> int:
        answer = 0

        for comb in combinations(range(len(needs[0])), r):
            comb = set(comb)
            count = 0
            for need in needs:
                for i, item in enumerate(need):
                    if i not in comb and item:
                        break
                else:
                    count += 1
            answer = max(answer, count)

        return answer


print(Solution.soulution(Solution, needs=[[1, 0, 0], [1, 1, 0], [1, 1, 0], [1, 0, 1], [1, 1, 0], [0, 1, 1]], r=2))
