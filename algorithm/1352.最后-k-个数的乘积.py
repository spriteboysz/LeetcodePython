#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-04-22 22:40:55
LastEditTime: 2022-04-22 22:44:13
Description: 
FilePath: 1352.最后-k-个数的乘积.py
"""
#
# @lc app=leetcode.cn id=1352 lang=python3
#
# [1352] 最后 K 个数的乘积
#

# @lc code=start

class ProductOfNumbers:
    def __init__(self):
        self.nums = [1]

    def add(self, num: int) -> None:
        if num == 0:
            self.nums = [1]
        else:
            self.nums.append(self.nums[-1] * num)

    def getProduct(self, k: int) -> int:
        if k >= len(self.nums):
            return 0
        else:
            return self.nums[-1] // self.nums[-k - 1]


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)
# @lc code=end
