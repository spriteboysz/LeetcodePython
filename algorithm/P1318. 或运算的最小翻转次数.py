#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-02-28 23:11:43
LastEditTime: 2022-02-28 23:18:18
Description: 
FilePath: 1318.或运算的最小翻转次数.py
"""


#
# @lc app=leetcode.cn id=1318 lang=python3
#
# [1318] 或运算的最小翻转次数
#

# @lc code=start
class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        count = 0
        for i in range(32):
            bit_a, bit_b, bit_c = (a >> i) & 1, (b >> i) & 1, (c >> i) & 1
            if bit_c == 0:
                count += bit_a + bit_b
            else:
                count += int(bit_a + bit_b == 0)
        return count

# @lc code=end
