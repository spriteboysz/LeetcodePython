#!/usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-01-25 23:12:12
LastEditTime: 2022-01-25 23:13:54
Description:
FilePath: 1455.检查单词是否为句中其他单词的前缀.py
"""
#
# @lc app=leetcode.cn id=1455 lang=python3
#
# [1455] 检查单词是否为句中其他单词的前缀
#

# @lc code=start
class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        for i, word in enumerate(sentence.strip().split()):
            if word.startswith(searchWord):
                return i + 1
        return -1
# @lc code=end
