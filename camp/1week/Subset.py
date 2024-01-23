
class Solution:
    def subset(self, nums):
        def backtrack(start, path):
            if path:
                result.append(path[:])

            for i in range(start, len(nums)):
                path.append(nums[i])
                backtrack(i + 1, path)
                path.pop()

        result = []
        backtrack(0, [])

        return result

print(Solution.subset(Solution, nums=[1,2,3]))