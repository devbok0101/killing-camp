import itertools
from typing import List


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def Queens(row, board):
            if row == n:
                res.append(["".join(r) for r in board])
                return
            print("=================================================")
            print("=====================재귀 시작=====================")
            for col in range(n):
                print("재귀 [검증 전]")
                print(f"Row, Col : {row}, {col}")
                print(board)
                print()
                if (
                        col not in vertical
                        and (row - col) not in diagonalLeft
                        and (row + col) not in diagonalRight
                ):
                    board[row][col] = "Q"
                    vertical.add(col)
                    diagonalLeft.add(row - col)
                    diagonalRight.add(row + col)
                    print("재귀 [재귀 시작 전]")
                    print(f"Row, Col : {row}, {col}")
                    print(board)
                    print()
                    Queens(row + 1, board)
                    board[row][col] = "."
                    vertical.remove(col)
                    diagonalLeft.remove(row - col)
                    diagonalRight.remove(row + col)
                    print("재귀 [재귀 종료 후]")
                    print(f"Row, Col : {row}, {col}")
                    print(board)
                    print()
            print("=====================재귀 종료=====================")
            print("=================================================")
        res = []
        board = [["." for _ in range(n)] for _ in range(n)]
        vertical, diagonalLeft, diagonalRight = set(), set(), set()
        Queens(0, board)
        return res

print(Solution.solveNQueens(Solution,n=2))
