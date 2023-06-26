#!/usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-01-30 22:10:45
LastEditTime: 2022-01-30 22:12:32
Description:
FilePath: 1837.k-进制表示下的各位数字总和.py
"""
#
# @lc app=leetcode.cn id=1837 lang=python3
#
# [1837] K 进制表示下的各位数字总和
#

# @lc code=start
class Solution:
    def sumBase(self, n: int, k: int) -> int:
        count = 0
        while n > 0:
            n, mod = divmod(n, k)
            count += mod
        return count
            
# @lc code=end

