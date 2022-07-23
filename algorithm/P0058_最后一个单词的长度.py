#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2022-01-07 22:26:11
LastEditTime: 2022-01-07 22:39:35
Description: 
FilePath: 58.最后一个单词的长度.py
'''
#
# @lc app=leetcode.cn id=58 lang=python3
#
# [58] 最后一个单词的长度
#

# @lc code=start
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        return len(s.strip().split()[-1])
# @lc code=end
