#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-02-16 22:37:45
LastEditTime: 2022-02-16 22:39:10
Description: 
FilePath: 386.字典序排数.py
"""
#
# @lc app=leetcode.cn id=386 lang=python3
#
# [386] 字典序排数
#

# @lc code=start
from typing import List


class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        return [i for i in sorted(range(1, n + 1), key=str)]


# @lc code=end
