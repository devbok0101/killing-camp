
from typing import List

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}
        def dp(amount):
            if amount == 0:
                return 0
            retList = []
            for coin in coins:
                if amount - coin >= 0:
                    if amount - coin not in memo:
                        memo[amount - coin] = dp(amount - coin)
                    if memo[amount - coin] != -1:
                        retList.append(memo[amount - coin])
            return min(retList) + 1 if retList else -1
        return dp(amount)



print(Solution.coinChange(Solution, coins=[1,2,5], amount=11))