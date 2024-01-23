from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        visited = []
        if root is None:
            return 0
        q = deque()
        q.append(root)

        while q:
            cur_node = q.popleft()
            visited.append(cur_node.val)

            if cur_node.left:
                visited.append(cur_node.left)
            if cur_node.right:
                visited.append(cur_node.right)

        list = visited[0]

        if not list:
            return 0
        else:
            return list[len(list)-1]


root = TreeNode([1, None, 2])

print(Solution.maxDepth(Solution, root))
