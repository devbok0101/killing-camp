import itertools
from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = list(itertools.permutations(nums))
        return ans

print(Solution.permute(Solution,nums=[1, 2, 3]))