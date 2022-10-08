#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2022-01-21 22:04:55
LastEditTime: 2022-01-21 22:08:33
Description: 
FilePath: 2114.句子中的最多单词数.py
'''
#
# @lc app=leetcode.cn id=2114 lang=python3
#
# [2114] 句子中的最多单词数
#

# @lc code=start
from typing import List


class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        return max(map(lambda el: len(el.split()), sentences))
# @lc code=end
