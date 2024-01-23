import itertools
from typing import List


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def isValid(current_bord, row, col):
            for i in range(row):
                if current_bord[i][col] == "Q":
                    return False
            i, j = row - 1, col - 1
            while i >= 0 and j >= 0:
                if current_bord[i][j] == "Q":
                    return False
                i -= 1
                j -= 1

            i, j = row - 1, col + 1
            while i >= 0 and j < n:
                if current_bord[i][j] == "Q":
                    return False
                i -= 1
                j += 1
            return True

        def backtrack(row):
            if row == n:
                result.append(["".join(row) for row in bord])
                return

            for col in range(n):
                if isValid(bord, row, col):
                    bord[row][col] = "Q"
                    backtrack(row + 1)
                    bord[row][col] = "."

        bord = [['.' for _ in range(n)] for _ in range(n)]
        result = []
        backtrack(0)
        return result

print(Solution.solveNQueens(Solution,n=2))
