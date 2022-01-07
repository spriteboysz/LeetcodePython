#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-10-04 20:10:16
Description: 
FilePath: 1816.截断句子.py
'''
#
# @lc app=leetcode.cn id=1816 lang=python3
#
# [1816] 截断句子
#

# @lc code=start


class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        return " ".join(s.split()[0:k])
# @lc code=end
