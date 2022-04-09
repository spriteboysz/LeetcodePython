#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-04-09 20:47:35
LastEditTime: 2022-04-09 20:52:06
Description: 
FilePath: 380.o-1-时间插入、删除和获取随机元素.py
"""
#
# @lc app=leetcode.cn id=380 lang=python3
#
# [380] O(1) 时间插入、删除和获取随机元素
#

# @lc code=start
from random import randint


class RandomizedSet:
    def __init__(self):
        self.lst = []

    def insert(self, val: int) -> bool:
        if val not in self.lst:
            self.lst.append(val)
            return True
        else:
            return False

    def remove(self, val: int) -> bool:
        if val not in self.lst:
            return False
        else:
            self.lst.remove(val)
            return True

    def getRandom(self) -> int:
        return self.lst[randint(0, len(self.lst) - 1)]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
# @lc code=end
