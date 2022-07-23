#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-03-14 00:10:09
LastEditTime: 2022-03-14 00:10:39
Description: 
FilePath: 677.键值映射.py
"""
#
# @lc app=leetcode.cn id=677 lang=python3
#
# [677] 键值映射
#

# @lc code=start
from collections import defaultdict


class MapSum:
    def __init__(self):
        self.map = defaultdict(int)

    def insert(self, key: str, val: int) -> None:
        self.map[key] = int(val)

    def sum(self, prefix: str) -> int:
        count = 0
        for k in self.map.keys():
            if k.startswith(prefix):
                count += self.map[k]
        return count


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)
# @lc code=end
