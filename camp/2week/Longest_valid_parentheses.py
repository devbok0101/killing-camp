from collections import deque
from typing import List


class Solution:
    def longestValidParentheses(self, s: str) -> int:
        longest = 0
        stack = [-1]
        for index, word in enumerate(s):
            if word == "(":
                stack.append(index)
            elif len(stack) == 1:
                stack[0] = index
            else:
                stack.pop()
                longest = max(longest, index - stack[-1])
        return longest


print(Solution.longestValidParentheses(Solution, s="(())"))
#)())()()()