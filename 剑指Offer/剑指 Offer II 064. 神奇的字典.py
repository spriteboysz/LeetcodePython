#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-06-05 22:24
LastEditTime: 2022-06-05 22:24
Description:
FilePath: 剑指 Offer II 064. 神奇的字典.py
"""

from typing import List


class MagicDictionary:

    def __init__(self):
        self.tree = []

    def buildDict(self, dictionary: List[str]) -> None:
        for word in dictionary:
            self.tree.append(word)

    def search(self, searchWord: str) -> bool:
        for word in self.tree:
            if len(word) != len(searchWord):
                continue
            if self.find(word, searchWord):
                return True
        return False

    def find(self, word, searchWord):
        count = 0
        for i in range(len(word)):
            if word[i] != searchWord[i]:
                if count == 0:
                    count += 1
                else:
                    return False
        return True if count else False
