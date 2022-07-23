#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2022-01-29 21:54:11
LastEditTime: 2022-01-29 21:56:09
Description: 
FilePath: 1791.找出星型图的中心节点.py
'''
#
# @lc app=leetcode.cn id=1791 lang=python3
#
# [1791] 找出星型图的中心节点
#

# @lc code=start
from typing import List


class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        if edges[0][0] in edges[1]:
            return edges[0][0]
        else:
            return edges[0][1]
# @lc code=end
