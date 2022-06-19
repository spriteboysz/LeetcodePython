#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-06-19 14:02
LastEditTime: 2022-06-19 14:02
Description:
FilePath: 剑指 Offer 49. 丑数.py
"""


class Solution:
    def nthUglyNumber(self, n: int) -> int:
        dp, a, b, c = [1] * n, 0, 0, 0
        for i in range(1, n):
            n2, n3, n5 = dp[a] * 2, dp[b] * 3, dp[c] * 5
            dp[i] = min(n2, n3, n5)
            if dp[i] == n2:
                a += 1
            if dp[i] == n3:
                b += 1
            if dp[i] == n5:
                c += 1
        # print(dp)
        return dp[-1]


if __name__ == '__main__':
    solution = Solution()
    ans = solution.nthUglyNumber(n=10)
    print(ans)
