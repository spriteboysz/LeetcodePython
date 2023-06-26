#!/usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-01-25 22:33:55
LastEditTime: 2022-01-25 22:39:28
Description:
FilePath: 1518.换酒问题.py
"""
#
# @lc app=leetcode.cn id=1518 lang=python3
#
# [1518] 换酒问题
#

# @lc code=start


class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        total = numBottles
        while numBottles >= numExchange:
            numBottles, mod = divmod(numBottles, numExchange)
            total += numBottles
            numBottles += mod
        return total
# @lc code=end


if __name__ == "__main__":
    s = Solution()
    print(s.numWaterBottles(2, 3))
