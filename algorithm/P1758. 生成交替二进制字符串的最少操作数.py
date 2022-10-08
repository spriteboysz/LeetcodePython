#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2022-01-30 22:20:40
LastEditTime: 2022-01-30 22:24:18
Description: 
FilePath: 1758.生成交替二进制字符串的最少操作数.py
'''
#
# @lc app=leetcode.cn id=1758 lang=python3
#
# [1758] 生成交替二进制字符串的最少操作数
#

# @lc code=start


class Solution:
    def minOperations(self, s: str) -> int:
        count1, count2 = 0, 0
        for i, item in enumerate(s):
            if item == "1":
                count1 += int(i % 2 == 0)
                count2 += int(i % 2 == 1)
            else:
                count1 += int(i % 2 == 1)
                count2 += int(i % 2 == 0)
        return min(count1, count2)

# @lc code=end
