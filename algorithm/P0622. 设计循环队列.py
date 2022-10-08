#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-06-03 22:49
LastEditTime: 2022-06-03 22:49
Description:
FilePath: 622.设计循环队列.py
"""


class MyCircularQueue:

    def __init__(self, k: int):
        self.queue = [0 for _ in range(k)]
        self.k = k
        self.front = 0
        self.rear = -1
        self.length = 0

    def enQueue(self, value: int) -> bool:
        if self.length < self.k:
            self.rear = (self.rear + 1) % self.k
            self.queue[self.rear] = value
            self.length += 1
            return True
        return False

    def deQueue(self) -> bool:
        if self.length > 0:
            self.front = (self.front + 1) % self.k
            self.length -= 1
            return True
        return False

    def Front(self) -> int:
        if self.length > 0:
            return self.queue[self.front]
        return -1

    def Rear(self) -> int:
        if self.length > 0:
            return self.queue[self.rear]
        return -1

    def isEmpty(self) -> bool:
        if self.length == 0:
            return True
        return False

    def isFull(self) -> bool:
        if self.length == self.k:
            return True
        return False
