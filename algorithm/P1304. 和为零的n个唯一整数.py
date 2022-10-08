#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2022-01-26 23:47:21
LastEditTime: 2022-01-26 23:51:02
Description: 
FilePath: 1304.和为零的n个唯一整数.py
'''
#
# @lc app=leetcode.cn id=1304 lang=python3
#
# [1304] 和为零的N个唯一整数
#

# @lc code=start
from typing import List


class Solution:
    def sumZero(self, n: int) -> List[int]:
        zero = []
        for i in range(1, int(n // 2) + 1):
            zero.extend([i, -i])
        if n % 2:
            zero.append(0)
        return zero
# @lc code=end
