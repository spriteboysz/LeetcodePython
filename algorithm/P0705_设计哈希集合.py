#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2022-02-06 16:25:30
LastEditTime: 2022-02-06 16:29:40
Description: 
FilePath: 705.设计哈希集合.py
'''
#
# @lc app=leetcode.cn id=705 lang=python3
#
# [705] 设计哈希集合
#

# @lc code=start
class MyHashSet:

    def __init__(self):
        self.lst = set()

    def add(self, key: int) -> None:
        self.lst.add(key)

    def remove(self, key: int) -> None:
        if key in self.lst:
            self.lst.remove(key)

    def contains(self, key: int) -> bool:
        return key in self.lst


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
# @lc code=end
