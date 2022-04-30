#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-02-20 23:04:10
LastEditTime: 2022-02-20 23:07:08
Description: 
FilePath: 100259.单词频率.py
"""
#
# @lc app=leetcode.cn id=100259 lang=python3
#
# [面试题 16.02] 单词频率
#

# @lc code=start
from typing import List
from collections import defaultdict


class WordsFrequency:
    def __init__(self, book: List[str]):
        self.words = defaultdict(int)
        for item in book:
            self.words[item] += 1

    def get(self, word: str) -> int:
        return self.words[word]


# Your WordsFrequency object will be instantiated and called as such:
# obj = WordsFrequency(book)
# param_1 = obj.get(word)
# @lc code=end
