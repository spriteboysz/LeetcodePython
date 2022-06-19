#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-06-19 21:16
LastEditTime: 2022-06-19 21:16
Description:
FilePath: 剑指 Offer 59 - II. 队列的最大值.py
"""

from collections import deque


class MaxQueue:

    def __init__(self):
        self.queue = deque()

    def max_value(self) -> int:
        if not self.queue:
            return -1
        return max(self.queue)

    def push_back(self, value: int) -> None:
        self.queue.append(value)

    def pop_front(self) -> int:
        if not self.queue:
            return -1
        return self.queue.popleft()
