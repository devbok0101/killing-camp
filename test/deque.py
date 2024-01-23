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
            elif not stack or stack.pop() != word:
                return False
        return not stack


print(Solution.isValid(Solution, "{}"))

# not stack == 스택이 비어있으면 true
