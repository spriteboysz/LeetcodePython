#!/usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-02-06 23:19:20
LastEditTime: 2022-02-06 23:24:31
Description:
FilePath: 1656.设计有序流.py
"""
#
# @lc app=leetcode.cn id=1656 lang=python3
#
# [1656] 设计有序流
#

# @lc code=start
from typing import List


class OrderedStream:

    def __init__(self, n: int):
        self.id = 1
        self.hash = {}

    def insert(self, idKey: int, value: str) -> List[str]:
        self.hash[idKey] = value
        ret = []
        while self.id in self.hash.keys():
            ret.append(self.hash[self.id])
            self.id += 1
        return ret


# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)
# @lc code=end
