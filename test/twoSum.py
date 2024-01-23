from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}

        for index, number in enumerate(nums):
            if number in dic:
                dic[number].append(index)
            else:
                dic[number] = [index]

        nums.sort()

        start, last = 0, len(nums)-1

        while start < last:
            if target > (nums[start] + nums[last]):
                start += 1
            elif target < (nums[start] + nums[last]):
                last -= 1
            else:
                return [dic[nums[start]][0], dic[nums[last]][-1]]


print(Solution.twoSum(Solution, [2, 7 ,11, 15], 9))



