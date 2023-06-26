#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-04-22 23:18:11
LastEditTime: 2022-04-22 23:22:03
Description: 
FilePath: 1381.设计一个支持增量操作的栈.py
"""


#
# @lc app=leetcode.cn id=1381 lang=python3
#
# [1381] 设计一个支持增量操作的栈
#

# @lc code=start
class CustomStack:
    def __init__(self, maxSize: int):
        self.max = maxSize
        self.stack = []

    def push(self, x: int) -> None:
        if len(self.stack) < self.max:
            self.stack.append(x)

    def pop(self) -> int:
        if self.stack:
            return self.stack.pop()
        else:
            return -1

    def increment(self, k: int, val: int) -> None:
        for i in range(min(len(self.stack), k)):
            self.stack[i] += val


# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)
# @lc code=end

if __name__ == "__main__":
    nums = [1, 2, 3, 4, 5]
