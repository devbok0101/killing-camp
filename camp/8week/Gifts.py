from collections import defaultdict
from typing import List


class Solution:
    def soulution(self, gift_cards: List[int], wants: List[int]) -> int:



        def rotate(now_state):
            for index, having_gift in enumerate(now_state):
                if having_gift == wants[index]:
                    continue
                for next in range(1, len(now_state)):
                    if having_gift == wants[next]:
                        ## 해당 index가 원하는 것을 가지고 있을 경우, temp에 저장
                        temp_gift = now_state[next]
                        # 바꿔주기
                        now_state[next] = having_gift
                        now_state[index] = temp_gift
                        break
                    elif having_gift != wants[next]:
                        continue

            return change_state

        def is_finish(result):
            count = 0
            for index, having in enumerate(result):
                if having != wants[index]:
                    count += 1
            return count > 1


        change_state = [gift for gift in gift_cards]
        result = rotate(change_state)

        before_result = [b for b in result]
        while before_result != result and is_finish(result):
            rotate(result)

        min_count = 0
        for index, having in enumerate(result):
            if having != wants[index]:
                min_count += 1
        return min_count


#print(Solution.soulution(Solution, gift_cards=[4, 5, 3, 2, 1], wants=[2, 4, 4, 5, 1]))
print(Solution.soulution(Solution, gift_cards=[5,4,5,4,5], wants=[1,2,3,5,4]))
