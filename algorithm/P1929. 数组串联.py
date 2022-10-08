#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2022-01-22 23:44:45
LastEditTime: 2022-01-22 23:45:15
Description: 
FilePath: 1929.数组串联.py
'''
#
# @lc app=leetcode.cn id=1929 lang=python3
#
# [1929] 数组串联
#

# @lc code=start
from typing import List


class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        return nums * 2
# @lc code=end
