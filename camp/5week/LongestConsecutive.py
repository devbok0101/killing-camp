from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        num_set = set(nums)
        answer = 0
        for number in num_set:
            before_number = number - 1
            if before_number not in num_set:
                add_number = 1
                while number + add_number in num_set:
                    add_number += 1
                answer = max(answer, add_number)
        return answer


print(Solution.longestConsecutive(Solution, nums=[100,4,200,1,3,2]))
