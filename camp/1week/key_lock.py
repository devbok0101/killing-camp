class Solution:
    def solution(key, lock):
        m = len(key)
        n = len(lock)

        keys = [[[0 for _ in range(m+2*n)] for _ in range(m+2*n)] for _ in range(4)]

        # 가운데에 원본, 90도 1회, 2회, 3회 만들어두기
        for i in range(m):
            for j in range(m):
                keys[0][n+i][n+j] = key[i][j]
                keys[1][n+j][m+n-1-i] = key[i][j]
                keys[2][m+n-1-i][m+n-1-j] = key[i][j]
                keys[3][m+n-1-j][n+i] = key[i][j]

        for k in keys:
            for i in range(m+n):
                for j in range(m+n):
                    flag = True
                    for ii in range(n):
                        for jj in range(n):
                            if not lock[ii][jj] ^ k[i+ii][j+jj]:
                                flag = False
                    if flag:
                        return True
        return False


print(Solution.solution(key=[[0, 0, 0], [1, 0, 0], [0, 1, 1]], lock=[[1, 1, 1], [1, 1, 0], [1, 0, 1]]))
