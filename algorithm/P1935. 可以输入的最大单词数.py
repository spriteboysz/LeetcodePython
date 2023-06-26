#!/usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-01-22 23:39:32
LastEditTime: 2022-01-22 23:44:27
Description:
FilePath: 1935.可以输入的最大单词数.py
"""
#
# @lc app=leetcode.cn id=1935 lang=python3
#
# [1935] 可以输入的最大单词数
#

# @lc code=start
class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        count = 0
        for word in text.split():
            for letter in brokenLetters:
                if letter in word:
                    break
            else:
                count += 1
        return count
# @lc code=end

