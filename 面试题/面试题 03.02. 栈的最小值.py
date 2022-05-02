#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-05-02 14:45:16
LastEditTime: 2022-05-02 14:45:17
Description: 
FilePath: 面试题 03.02. 栈的最小值.py
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

    def getMin(self) -> int:
        return self.minimum[-1]
