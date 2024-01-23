from collections import deque


class Solution:
    def solution(self, queue1, queue2):
        que1 = deque(queue1)
        que2 = deque(queue2)
        sum_que1 = sum(que1)
        sum_que2 = sum(que2)
        max_cycle = len(que1) * 3

        if (sum_que1 + sum_que2) % 2 != 0:
            return -1

        count = 0

        while que1 and que2:
            if count > max_cycle:
                return -1

            if sum_que2 > sum_que1:
                popped_number = que2.popleft()
                que1.append(popped_number)
                sum_que2 -= popped_number
                sum_que1 += popped_number
                count += 1
            elif sum_que1 > sum_que2:
                popped_number = que1.popleft()
                que2.append(popped_number)
                sum_que1 -= popped_number
                sum_que2 += popped_number
                count += 1
            elif sum_que1 == sum_que2:
                return count

        if not que2 or not que1:
            return -1
        return count


print(Solution.solution(Solution, queue1=[1,2,3,4], queue2=[5,6,7,18]))
