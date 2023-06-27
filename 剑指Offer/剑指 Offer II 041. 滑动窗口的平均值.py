#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-05-16 23:12:52
LastEditTime: 2022-05-16 23:15:23
Description:
FilePath: 剑指 Offer II 041. 滑动窗口的平均值.py
"""
#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-05-16 23:12:52
LastEditTime: 2022-05-16 23:12:53
Description: 
FilePath: 剑指 Offer II 041. 滑动窗口的平均值.py
"""

from collections import deque


class MovingAverage:
    def __init__(self, size: int):
        """
        Initialize your data structure here.
        """
        self.size = size
        self.queue = deque()
        self.total = 0

    def next(self, val: int) -> float:
        self.queue.append(val)
        self.total += val

        if len(self.queue) > self.size:
            self.total -= self.queue.popleft()
        return self.total / len(self.queue)


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)
