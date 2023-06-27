#!/usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-02-02 22:29:33
LastEditTime: 2022-02-02 22:47:55
Description:
FilePath: 941.有效的山脉数组.py
"""
#
# @lc app=leetcode.cn id=941 lang=python3
#
# [941] 有效的山脉数组
#

# @lc code=start
from typing import List


class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr) <= 2 or arr[0] >= arr[1]:
            return False

        flag = True
        for i in range(2, len(arr)):
            if flag and arr[i - 1] >= arr[i]:
                flag = False
            if not flag and arr[i - 1] <= arr[i]:
                return False
        return not flag

# @lc code=end
