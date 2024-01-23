from collections import defaultdict
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        answer = defaultdict(list)

        for index, number in enumerate(nums):
            answer[number].append(index)

        nums.sort()

        left, right = 0, len(nums) - 1

        while left < right:
            if target > nums[left] + nums[right]:
                left += 1
            elif target < nums[left] + nums[right]:
                right -= 1
            else:
                return [answer[nums[left]][0], answer[nums[right]][-1]]


print(Solution.twoSum(Solution, nums=[2, 4, 6, 8, 2], target=14))
