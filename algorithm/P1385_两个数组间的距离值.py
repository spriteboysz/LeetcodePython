#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2022-01-26 22:42:32
LastEditTime: 2022-01-26 22:44:59
Description: 
FilePath: 1385.两个数组间的距离值.py
'''
#
# @lc app=leetcode.cn id=1385 lang=python3
#
# [1385] 两个数组间的距离值
#

# @lc code=start
from typing import List


class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        count = 0
        for num in arr1:
            if all(list(map(lambda el: abs(num - el) > d, arr2))):
                count += 1
        return count
# @lc code=end
