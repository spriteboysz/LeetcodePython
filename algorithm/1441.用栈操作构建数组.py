#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2022-01-25 23:16:37
LastEditTime: 2022-01-25 23:20:49
Description: 
FilePath: 1441.用栈操作构建数组.py
'''
#
# @lc app=leetcode.cn id=1441 lang=python3
#
# [1441] 用栈操作构建数组
#

# @lc code=start
from typing import List


class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        operator = []
        for i in range(1, max(target) + 1):
            operator.append("Push")
            if i not in target:
                operator.append("Pop")
        return operator
# @lc code=end
