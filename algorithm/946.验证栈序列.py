#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-03-09 22:51:38
LastEditTime: 2022-03-09 22:53:37
Description: 
FilePath: 946.验证栈序列.py
"""
#
# @lc app=leetcode.cn id=946 lang=python3
#
# [946] 验证栈序列
#

# @lc code=start
from typing import List


class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack, index = [], 0
        for item in pushed:
            stack.append(item)
            while stack and stack[-1] == popped[index]:
                stack.pop()
                index += 1
        return index == len(popped)


# @lc code=end
