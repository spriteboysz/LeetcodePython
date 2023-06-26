#!/usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-01-30 22:27:47
LastEditTime: 2022-01-30 22:30:00
Description:
FilePath: 1720.解码异或后的数组.py
"""
#
# @lc app=leetcode.cn id=1720 lang=python3
#
# [1720] 解码异或后的数组
#

# @lc code=start
from typing import List


class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        decode = [first]
        for item in encoded:
            first ^= item
            decode.append(first)
        return decode
# @lc code=end
