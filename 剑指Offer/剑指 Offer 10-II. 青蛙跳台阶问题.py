#!/usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-02-04 22:45:22
LastEditTime: 2022-02-04 22:50:42
Description:
FilePath: 100277.青蛙跳台阶问题.py
"""
#
# @lc app=leetcode.cn id=100277 lang=python3
#
# [剑指 Offer 10- II] 青蛙跳台阶问题
#

# @lc code=start
class Solution:
    def numWays(self, n: int) -> int:
        if n == 0 or n == 1:
            return 1
        else:
            a, b = 1, 1
            for _ in range(2, n + 1):
                a, b = a + b, a
            return a % (10 ** 9 + 7)
# @lc code=end


if __name__ == "__main__":
    s = Solution()
    print(s.numWays(2))
    print(s.numWays(7))
    print(s.numWays(0))
