#!/usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-02-06 16:30:45
LastEditTime: 2022-02-06 16:36:42
Description:
FilePath: 706.设计哈希映射.py
"""
#
# @lc app=leetcode.cn id=706 lang=python3
#
# [706] 设计哈希映射
#

# @lc code=start


class MyHashMap:

    def __init__(self):
        self.hash = dict()

    def put(self, key: int, value: int) -> None:
        self.hash[key] = value

    def get(self, key: int) -> int:
        if key in self.hash.keys():
            return self.hash[key]
        else:
            return -1

    def remove(self, key: int) -> None:
        if key in self.hash.keys():
            self.hash.pop(key)


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
# @lc code=end
