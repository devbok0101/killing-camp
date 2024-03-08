from collections import defaultdict, Counter
from typing import List


class Solution:
    def soulution(self, gift_cards: List[int], wants: List[int]) -> int:
        answer = 0
        counter = Counter(gift_cards)
        for want in wants:
            if want in counter and counter[want] != 0:
                counter[want] -= 1
            else:
                answer += 1

        return answer


#print(Solution.soulution(Solution, gift_cards=[4, 5, 3, 2, 1], wants=[2, 4, 4, 5, 1]))
print(Solution.soulution(Solution, gift_cards=[5,4,5,4,5], wants=[1,2,3,5,4]))
