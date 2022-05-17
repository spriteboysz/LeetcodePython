#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-05-17 23:24:42
LastEditTime: 2022-05-17 23:24:43
Description: 
FilePath: 剑指 Offer II 066. 单词之和.py
"""

from collections import defaultdict


class MapSum:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.words = defaultdict(int)

    def insert(self, key: str, val: int) -> None:
        self.words[key] = val

    def sum(self, prefix: str) -> int:
        return sum([v for k, v in self.words.items() if k.startswith(prefix)])
        # count = 0
        # for k, v in self.words.items():
        #     if k.startswith(prefix):
        #         count += v
        # return count
