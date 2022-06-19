#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-06-19 14:49
LastEditTime: 2022-06-19 14:49
Description:
FilePath: 剑指 Offer 41. 数据流中的中位数.py
"""


class MedianFinder:

    def __init__(self):
        self.store = []

    def addNum(self, num: int) -> None:
        self.store.append(num)

    def findMedian(self) -> float:
        self.store.sort()
        n = len(self.store)
        if n & 1 == 1:  # n 是奇数
            return self.store[n // 2]
        else:
            return (self.store[n // 2 - 1] + self.store[n // 2]) / 2
