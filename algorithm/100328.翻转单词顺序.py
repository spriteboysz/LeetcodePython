#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2022-02-04 14:09:11
LastEditTime: 2022-02-04 14:09:51
Description: 
FilePath: 100328.翻转单词顺序.py
'''
#
# @lc app=leetcode.cn id=100328 lang=python3
#
# [剑指 Offer 58 - I] 翻转单词顺序
#

# @lc code=start
class Solution:
    def reverseWords(self, s: str) -> str:
        return " ".join(s.strip().split()[::-1])
# @lc code=end

