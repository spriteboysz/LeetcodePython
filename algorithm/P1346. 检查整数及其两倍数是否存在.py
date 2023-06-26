#!/usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-01-26 23:02:46
LastEditTime: 2022-01-26 23:04:40
Description:
FilePath: 1346.检查整数及其两倍数是否存在.py
"""
#
# @lc app=leetcode.cn id=1346 lang=python3
#
# [1346] 检查整数及其两倍数是否存在
#

# @lc code=start
from typing import List


class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        if arr.count(0) >= 2:
            return True
        else:
            for item in sorted(arr):
                if item != 0 and 2 * item in arr:
                    return True
            return False
# @lc code=end
