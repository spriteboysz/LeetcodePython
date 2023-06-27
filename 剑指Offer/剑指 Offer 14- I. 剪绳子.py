#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-05-26 23:46
LastEditTime: 2022-05-26 23:46
Description:
FilePath: 剑指 Offer 14- I. 剪绳子
"""


class Solution:
    def cuttingRope(self, n: int) -> int:
        dp = [0 for i in range(n + 2)]
        for i in range(2, n + 1):
            cur = 0
            for j in range(1, i):
                cur = max(cur, max(j * (i - j), j * dp[i - j]))
            dp[i] = cur
        return dp[i]


if __name__ == '__main__':
    solution = Solution()
    ans = solution.cuttingRope(10)
    print(ans)
