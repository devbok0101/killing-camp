import itertools
from bisect import bisect_left
from math import inf
from typing import List
from math import factorial


class Solution:
    def minimumDifference(self, nums: List[int]) -> int:
        ans = inf
        goal = sum(nums) / 2

        def add_subset(lst):
            result = [[] for _ in range(0, len(lst)+1)]
            for i in range(0, len(lst)+1):
                for comb in itertools.combinations(lst, i):
                    result[i].append(sum(comb))
            return result

        lefts = add_subset(nums[:len(nums)//2])
        rights = add_subset(nums[len(nums)//2:])
        for i, left in enumerate(lefts):
            right = sorted(rights[len(rights)-1-i])
            for j in left:
                k = bisect_left(right, goal-j)
                if k < len(right):
                    ans = min(ans, right[k] + j - goal)
        return int(ans*2)

print(Solution.minimumDifference(Solution,nums = [3,9,7,3]))