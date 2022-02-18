#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-02-18 22:26:46
LastEditTime: 2022-02-18 22:42:56
Description: 
FilePath: 2166.设计位集.py
"""
#
# @lc app=leetcode.cn id=2166 lang=python3
#
# [2166] 设计位集
#

# @lc code=start
class Bitset:
    def __init__(self, size: int):
        self.cnt, self.size = 0, size
        self.bitset = [0] * size
        self.backup = [1] * size

    def fix(self, idx: int) -> None:
        if self.bitset[idx] == 0:
            self.cnt += 1
            self.bitset[idx] = 1
            self.backup[idx] = 0

    def unfix(self, idx: int) -> None:
        if self.bitset[idx] == 1:
            self.cnt -= 1
            self.bitset[idx] = 0
            self.backup[idx] = 1

    def flip(self) -> None:
        self.bitset, self.backup = self.backup, self.bitset
        self.cnt = self.size - self.cnt
        
    def all(self) -> bool:
        return self.cnt == self.size

    def one(self) -> bool:
        return self.cnt > 0

    def count(self) -> int:
        return self.cnt

    def toString(self) -> str:
        return "".join(map(str, self.bitset))


# Your Bitset object will be instantiated and called as such:
# obj = Bitset(size)
# obj.fix(idx)
# obj.unfix(idx)
# obj.flip()
# param_4 = obj.all()
# param_5 = obj.one()
# param_6 = obj.count()
# param_7 = obj.toString()
# @lc code=end
