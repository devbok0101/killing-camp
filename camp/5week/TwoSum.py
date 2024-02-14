from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        memo = {}

        for index, num_a in enumerate(nums):
            numb_b = target - num_a
            if numb_b in memo:
                return [memo[numb_b], index]
            memo[num_a] = index


print(Solution.twoSum(Solution, nums=[2, 4, 6, 8, 2], target=14))
