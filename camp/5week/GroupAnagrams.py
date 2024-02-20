from collections import defaultdict
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        result = defaultdict(list)

        for word in strs:
            spells = [char for char in word]
            spells.sort()
            result[tuple(spells)].append(word)

        return list(result.values())


print(Solution.groupAnagrams(Solution, strs=["eat","tea","tan","ate","nat","bat"]))