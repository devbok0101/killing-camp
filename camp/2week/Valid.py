from collections import defaultdict
from typing import List


class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for word in s:
            if "(" == word:
                stack.append(")")
            elif "{" == word:
                stack.append("}")
            elif "[" == word:
                stack.append("]")
            elif stack and word == stack[-1]:
                stack.pop()
            else:
                return False

        return not stack


print(Solution.isValid(Solution, s="({[]}]"))
