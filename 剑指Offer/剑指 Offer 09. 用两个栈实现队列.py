#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-05-20 22:35:04
LastEditTime: 2022-05-20 22:35:04
Description: 
FilePath: 剑指 Offer 09. 用两个栈实现队列.py
"""


class CQueue:
    def __init__(self):
        self.stack1, self.stack2 = [], []

    def appendTail(self, value: int) -> None:
        self.stack1.append(value)

    def deleteHead(self) -> int:
        if self.stack2:
            return self.stack2.pop()
        if not self.stack1:
            return -1
        while self.stack1:
            self.stack2.append(self.stack1.pop())
        return self.stack2.pop()


# Your CQueue object will be instantiated and called as such:
# obj = CQueue()
# obj.appendTail(value)
# param_2 = obj.deleteHead()
