#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2022-02-07 23:35:52
LastEditTime: 2022-02-07 23:36:43
Description: 
FilePath: 1000017.阶乘尾数.py
'''
#
# @lc app=leetcode.cn id=1000017 lang=python3
#
# [面试题 16.05] 阶乘尾数
#

# @lc code=start


class Solution:
    def trailingZeroes(self, n: int) -> int:
        count = 0
        while n > 1:
            count += n // 5
            n //= 5
        return count


# @lc code=end
