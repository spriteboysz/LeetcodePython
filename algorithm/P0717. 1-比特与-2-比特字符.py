#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-04-11 23:42:32
LastEditTime: 2022-04-11 23:45:26
Description: 
FilePath: 717.1-比特与-2-比特字符.py
"""
#
# @lc app=leetcode.cn id=717 lang=python3
#
# [717] 1 比特与 2 比特字符
#

# @lc code=start
from typing import List


class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        n, index = len(bits), 0
        if n == 1 or bits[-2] == 0:
            return True
        while index < n - 1:
            if bits[index] == 1:
                index += 2
            else:
                index += 1
        return index == n - 1


# @lc code=end
