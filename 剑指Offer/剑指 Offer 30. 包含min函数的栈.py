#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-05-01 21:32:52
LastEditTime: 2022-05-01 21:36:06
Description: 
FilePath: 剑指 Offer 30. 包含min函数的栈.py
"""


class MinStack:
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack, self.minimum = [], []

    def push(self, x: int) -> None:
        self.stack.append(x)
        if not self.minimum or self.minimum[-1] >= x:
            self.minimum.append(x)

    def pop(self) -> None:
        if self.stack.pop() == self.minimum[-1]:
            self.minimum.pop()

    def top(self) -> int:
        return self.stack[-1]

    def min(self) -> int:
        return self.minimum[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.min()
