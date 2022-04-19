#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-04-19 23:26:50
LastEditTime: 2022-04-19 23:29:05
Description:
FilePath: 211.添加与搜索单词-数据结构设计.py
"""
#
# @lc app=leetcode.cn id=211 lang=python3
#
# [211] 添加与搜索单词 - 数据结构设计
#

# @lc code=start
from collections import defaultdict
from re import search


class WordDictionary:
    def __init__(self):
        self.dictionary = defaultdict(set)

    def addWord(self, word: str) -> None:
        self.dictionary[len(word)].add(word)

    def search(self, word: str) -> bool:
        if len(word) not in self.dictionary:
            return False
        for value in self.dictionary[len(word)]:
            if search(word, value, flags=0):
                return True
        return False


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
# @lc code=end
