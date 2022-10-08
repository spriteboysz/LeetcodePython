#! /usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2022-02-19 22:52:06
LastEditTime: 2022-02-19 22:53:02
Description: 
FilePath: 151.翻转字符串里的单词.py
'''
#
# @lc app=leetcode.cn id=151 lang=python3
#
# [151] 翻转字符串里的单词
#

# @lc code=start
class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.strip().split()
        return " ".join(words[::-1])
# @lc code=end

