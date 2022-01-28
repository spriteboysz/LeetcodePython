#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2022-01-28 21:59:46
LastEditTime: 2022-01-28 22:02:33
Description: 
FilePath: 1122.数组的相对排序.py
'''
#
# @lc app=leetcode.cn id=1122 lang=python3
#
# [1122] 数组的相对排序
#

# @lc code=start
from typing import List
from math import inf


class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        return list(sorted(arr1, key=lambda el: (arr2.index(el) if el in arr2 else inf, el)))
# @lc code=end
