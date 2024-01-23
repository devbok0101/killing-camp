from typing import List


class Solution:
    def solution(self, relation):
        width = len(relation[0])

        candidate_keys = []

        def gen_combinations(start, depth, max_depth, curr, result_combs):
            if depth == max_depth:
                result_combs.append(curr[:])
                return

            for i in range(start, width):
                curr.append(i)
                gen_combinations(i + 1, depth + 1, max_depth, curr, result_combs)
                curr.pop()

        for length in range(1, width + 1):
            combinations = []
            gen_combinations(0, 0, length, [], combinations)

            for cols in combinations:
                minimality = True
                row_set = set()

                # 최소성 검사
                for key in candidate_keys:
                    # A.issubset(B) -> A가 B의 부분집합인가?
                    if set(key).issubset(set(cols)):
                        minimality = False
                        break
                if not minimality:
                    continue

                # 유일성
                height = len(relation)
                for r in relation:
                    # 이렇게 더해서 문자열로 비교해도 되겠구나?
                    row_str = "".join(r[index] for index in cols)
                    row_set.add(row_str)

                if len(row_set) == height:
                    candidate_keys.append(cols)

        return len(candidate_keys)


print(Solution.solution(Solution, relation=[["100", "ryan", "music", "2"], ["200", "apeach", "math", "2"],
                                            ["300", "tube", "computer", "3"], ["400", "con", "computer", "4"],
                                            ["500", "muzi", "music", "3"], ["600", "apeach", "music", "2"]]))
