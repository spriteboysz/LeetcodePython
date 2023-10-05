#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2023-10-03 11:39
FileName: LCP
Description:LCR 125. 图书整理 II.py 
"""
from collections import deque


class CQueue:

    def __init__(self):
        self.queue = deque()

    def appendTail(self, value: int) -> None:
        self.queue.append(value)

    def deleteHead(self) -> int:
        return self.queue.popleft() if self.queue else -1


if __name__ == '__main__':
    obj = CQueue()
    obj.appendTail(1)
    obj.appendTail(2)
    print(obj.deleteHead())
