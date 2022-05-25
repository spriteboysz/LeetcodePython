#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-05-25 23:07
LastEditTime: 2022-05-25 23:07
Description:
FilePath: 面试题 10.10. 数字流的秩.py
"""

from bisect import insort, bisect


class StreamRank:

    def __init__(self):
        self.stream = []

    def track(self, x: int) -> None:
        insort(self.stream, x)

    def getRankOfNumber(self, x: int) -> int:
        if x in self.stream:
            return self.stream.index(x) + self.stream.count(x)
        else:
            return bisect(self.stream, x)
