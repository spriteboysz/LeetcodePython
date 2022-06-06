#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-06-06 23:23
LastEditTime: 2022-06-06 23:23
Description:
FilePath: 剑指 Offer II 103. 最少的硬币数目.py
"""

from typing import List
from math import inf


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        coins.sort()
        if coins[0] > amount:
            return -1

        dp = [0] + [inf] * amount
        for coin in coins:
            for i in range(coin, amount + 1):
                dp[i] = min(dp[i], dp[i - coin] + 1)
        return dp[-1] if dp[-1] != inf else -1


if __name__ == '__main__':
    solution = Solution()
    ans = solution.coinChange(coins=[1, 2, 5], amount=11)
    print(ans)
