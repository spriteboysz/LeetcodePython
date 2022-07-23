#!/usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-02-12 22:58:48
LastEditTime: 2022-02-19 23:08:44
Description: 
FilePath: 322.零钱兑换.py
"""
#
# @lc app=leetcode.cn id=322 lang=python3
#
# [322] 零钱兑换
#

# @lc code=start
from math import inf
from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [0] + [inf] * amount
        for i in range(1, amount + 1):
            for coin in filter(lambda coin: i - coin >= 0, coins):
                dp[i] = min(dp[i], dp[i - coin] + 1)

        return -1 if dp[amount] == inf else dp[amount]


# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    ans = solution.coinChange([1, 2, 5], 108)
    print(ans)
    ans = solution.coinChange([2], 3)
    print(ans)
