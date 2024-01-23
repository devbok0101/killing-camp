from collections import deque
from typing import List


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        if not s:
            return []

        def backtrack(s, start, partitions, lists):
            if start == len(s):
                lists.append(partitions[:])
                return

            for i in range(start + 1, len(s) + 1):
                tmp_str = s[start:i]
                if tmp_str == tmp_str[::-1]:
                    partitions.append(tmp_str)
                    backtrack(s, i, partitions, lists)
                    partitions.pop()

        lists = []
        partitions = []

        backtrack(s, 0, partitions, lists)

        return lists

    def combine(self, n: int, k: int) -> List[List[int]]:
        def backtrack(start, path):
            if len(path) == k:
                result.append(path[:])
                return

            for i in range(start, n + 1):
                path.append(i)
                backtrack(i + 1, path)
                path.pop()

        result = []
        backtrack(1, [])

        return result


#print(Solution.partition(Solution, s="aab"))
print(Solution.combine(Solution, n=4, k=2))
