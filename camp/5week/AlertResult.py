from collections import defaultdict


class Solution:
    def solution(self, id_list, report, k):

        reporters = defaultdict(list)
        reported_people = defaultdict(int)
        mail = defaultdict(int)
        answer = []
        for result in report:
            result_split = result.split()
            reporter = result_split[0]
            reported_person = result_split[1]
            if reported_person not in reporters[reporter]:
                reporters[reporter].append(reported_person)
                reported_count = reported_people[reported_person]
                if reported_person in reported_people:
                    reported_count += 1
                    reported_people[reported_person] = reported_count

        for user in id_list:
            for badMan in reporters[user]:
                total_count = reported_people[badMan]
                if total_count >= k:
                    mail[user] += 1

        for result_user in id_list:
            answer.append(mail[result_user])

        return answer


# print(Solution.solution(Solution, id_list=["con", "ryan"], report=["ryan con", "ryan con", "ryan con", "ryan con"], k=2))
print(Solution.solution(Solution, id_list=["muzi", "frodo", "apeach", "neo"],
                        report=["muzi frodo", "apeach frodo", "frodo neo", "muzi neo", "apeach muzi"], k=2))
