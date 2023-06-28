#!/usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-02-07 23:38:25
LastEditTime: 2022-02-07 23:40:04
Description:
FilePath: 100170.化栈为队.py
"""
#
# @lc app=leetcode.cn id=100170 lang=python3
#
# [面试题 03.04] 化栈为队
#

# @lc code=start


class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.queue = []

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.queue.append(x)

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        return self.queue.pop(0)

    def peek(self) -> int:
        """
        Get the front element.
        """
        return self.queue[0]

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return self.queue == []


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
# @lc code=end
