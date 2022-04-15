#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-04-15 22:28:38
LastEditTime: 2022-04-15 22:36:04
Description: 
FilePath: 1663.具有给定数值的最小字符串.py
"""
#
# @lc app=leetcode.cn id=1663 lang=python3
#
# [1663] 具有给定数值的最小字符串
#

# @lc code=start
from string import ascii_lowercase as lower


class Solution:
    def getSmallestString(self, n: int, k: int) -> str:
        # s = a * i + "x" + z * j
        for i in range(n, -1, -1):
            j = n - i - 1
            x = k - 26 * j - i
            if 1 <= x <= 26 and j >= 0:
                print(i, x, j)
                return "a" * i + lower[x - 1] + "z" * j


# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    ans = solution.getSmallestString(3, 27)
    print(ans)
    ans = solution.getSmallestString(2, 52)
    print(ans)
