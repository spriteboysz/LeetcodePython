#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-04-29 23:41:26
LastEditTime: 2022-04-29 23:48:37
Description: 
FilePath: 676.实现一个魔法字典.py
"""
#
# @lc app=leetcode.cn id=676 lang=python3
#
# [676] 实现一个魔法字典
#

# @lc code=start
from collections import defaultdict
from typing import List


class MagicDictionary:
    def __init__(self):
        self.dict = defaultdict(list)

    def buildDict(self, dictionary: List[str]) -> None:
        for word in dictionary:
            self.dict[len(word)].append(word)

    def search(self, searchWord: str) -> bool:
        if len(searchWord) not in self.dict:
            return False
        for word in self.dict[len(searchWord)]:
            if self.find(word, searchWord):
                return True
        return False

    def find(self, word, searchWord):  # 匹配字符
        count = 0
        for s, t in zip(searchWord, word):
            if s == t:
                continue
            if count == 0:
                count += 1
            else:
                return False
        return True if count else False  # 必须修改一次


# Your MagicDictionary object will be instantiated and called as such:
# obj = MagicDictionary()
# obj.buildDict(dictionary)
# param_2 = obj.search(searchWord)
# @lc code=end
