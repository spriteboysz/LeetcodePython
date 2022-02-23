#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-02-23 22:21:36
LastEditTime: 2022-02-23 22:25:13
Description: 
FilePath: 648.单词替换.py
"""
#
# @lc app=leetcode.cn id=648 lang=python3
#
# [648] 单词替换
#

# @lc code=start
from typing import List


class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        dic = set(dictionary)

        def replace(word):
            for i in range(len(word)):
                if word[:i] in dic:
                    return word[:i]
            return word

        return " ".join(map(replace, sentence.split()))


# @lc code=end
