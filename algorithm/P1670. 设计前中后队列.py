#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-04-19 22:47:30
LastEditTime: 2022-04-19 22:50:32
Description: 
FilePath: 1670.设计前中后队列.py
"""


#
# @lc app=leetcode.cn id=1670 lang=python3
#
# [1670] 设计前中后队列
#

# @lc code=start
class FrontMiddleBackQueue:
    def __init__(self):
        self.queue = []

    def pushFront(self, val: int) -> None:
        self.queue.insert(0, val)

    def pushMiddle(self, val: int) -> None:
        self.queue.insert(len(self.queue) // 2, val)

    def pushBack(self, val: int) -> None:
        self.queue.append(val)

    def popFront(self) -> int:
        return self.queue.pop(0) if self.queue else -1

    def popMiddle(self) -> int:
        return self.queue.pop((len(self.queue) - 1) // 2) if self.queue else -1

    def popBack(self) -> int:
        return self.queue.pop() if self.queue else -1

# Your FrontMiddleBackQueue object will be instantiated and called as such:
# obj = FrontMiddleBackQueue()
# obj.pushFront(val)
# obj.pushMiddle(val)
# obj.pushBack(val)
# param_4 = obj.popFront()
# param_5 = obj.popMiddle()
# param_6 = obj.popBack()
# @lc code=end
