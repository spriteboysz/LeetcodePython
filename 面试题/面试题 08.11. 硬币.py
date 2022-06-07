#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-06-07 22:44
LastEditTime: 2022-06-07 22:44
Description:
FilePath: 面试题 08.11. 硬币.py
"""

class Solution:
    def waysToChange(self, n: int) -> int:
        coins = [1, 5, 10, 25]
        dp = [1] + [0] * n
        for coin in coins:
            for i in range(coin, n + 1):
                dp[i] += dp[i - coin]
        # print(dp)
        return dp[n] % 1000000007

if __name__ == '__main__':
    solution = Solution()
    ans = solution.waysToChange(10)
    print(ans)
