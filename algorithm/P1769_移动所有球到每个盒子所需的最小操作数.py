#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2022-02-15 22:23:13
LastEditTime: 2022-02-15 22:31:31
Description: 
FilePath: 1769.移动所有球到每个盒子所需的最小操作数.py
'''
#
# @lc app=leetcode.cn id=1769 lang=python3
#
# [1769] 移动所有球到每个盒子所需的最小操作数
#

# @lc code=start
from typing import List


class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        counts = [0] * len(boxes)
        for i in range(len(boxes)):
            for j in range(len(boxes)):
                if j != i and boxes[j] == "1":
                    counts[i] += abs(j - i)
        return counts
# @lc code=end
