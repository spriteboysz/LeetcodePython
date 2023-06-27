#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-02-16 00:07:56
LastEditTime: 2022-02-18 23:23:52
Description: 
FilePath: 50.pow-x-n.py
"""


#
# @lc app=leetcode.cn id=50 lang=python3
#
# [50] Pow(x, n)
#

# @lc code=start
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            x = 1 / x
            n = abs(n)
        power = 1
        while n:
            if n & 1:
                power *= x
            x *= x
            n >>= 1
        return power


# @lc code=end


if __name__ == "__main__":
    s = Solution()
    print(s.myPow(2.0, 0))
