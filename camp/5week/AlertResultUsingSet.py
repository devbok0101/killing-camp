
class Solution:
    def solution(self, id_list, report, k):

        report_set = set(report)
        answer = [0] * len(id_list)

        reporters = {reporter: 0 for reporter in id_list}

        for r in report_set:
            reported_person = r.split()[1]
            reporters[reported_person] += 1

        for r in report_set:
            reporter = r.split()[0]
            reported_person = r.split()[1]
            if reporters[reported_person] >= k:
                answer[id_list.index(reporter)] += 1

        return answer


# print(Solution.solution(Solution, id_list=["con", "ryan"], report=["ryan con", "ryan con", "ryan con", "ryan con"], k=2))
print(Solution.solution(Solution, id_list=["muzi", "frodo", "apeach", "neo"],
                        report=["muzi frodo", "apeach frodo", "frodo neo", "muzi neo", "apeach muzi"], k=2))
