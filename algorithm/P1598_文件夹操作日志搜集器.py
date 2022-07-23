#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2022-01-24 23:44:40
LastEditTime: 2022-01-24 23:49:51
Description: 
FilePath: 1598.文件夹操作日志搜集器.py
'''
#
# @lc app=leetcode.cn id=1598 lang=python3
#
# [1598] 文件夹操作日志搜集器
#

# @lc code=start
from typing import List
class Solution:
    def minOperations(self, logs: List[str]) -> int:
        depth = 0
        for log in logs:
            if log == "../":
                if depth > 0:
                    depth -= 1
            elif log != "./":
                depth += 1
        return depth
# @lc code=end

