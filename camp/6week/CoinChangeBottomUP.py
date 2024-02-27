
from typing import List

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [10**4+1 for _ in range(amount + 1)]
        dp[0] = 0

        for i in range(amount + 1):
            for coin in coins:
                if i + coin <= amount:
                    dp[i + coin] = min(dp[i + coin], dp[i] + 1)

        return -1 if dp[amount] == 10**4+1 else dp[amount]



print(Solution.coinChange(Solution, coins=[1,2,5], amount=11))