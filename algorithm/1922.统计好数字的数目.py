#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-03-11 22:49:35
LastEditTime: 2022-03-11 22:54:02
Description: 
FilePath: 1922.统计好数字的数目.py
"""
#
# @lc app=leetcode.cn id=1922 lang=python3
#
# [1922] 统计好数字的数目
#

# @lc code=start
from math import ceil, floor


class Solution:
    def countGoodNumbers(self, n: int) -> int:
        mod = 10 ** 9 + 7
        a = pow(5, ceil(n / 2), mod)
        b = pow(4, floor(n / 2), mod)
        return (a * b) % mod


# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    ans = solution.countGoodNumbers(1)
    print(ans)
    ans = solution.countGoodNumbers(4)
    print(ans)
    ans = solution.countGoodNumbers(50)
    print(ans)
