#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-05-02 20:32
FileName: algorithm
Description:P2336. 无限集中的最小数字.py 
"""
import heapq


class SmallestInfiniteSet:

    def __init__(self):
        self.visited = [False] * 1010
        self.queue = []
        self.index = 1

    def popSmallest(self) -> int:
        if self.queue:
            ans = heapq.heappop(self.queue)
            self.visited[ans] = False
        else:
            ans = self.index
            self.index += 1
        return ans

    def addBack(self, num: int) -> None:
        if num >= self.index or self.visited[num]:
            return
        if num == self.index - 1:
            self.index -= 1
        else:
            heapq.heappush(self.queue, num)
            self.visited[num] = True


if __name__ == '__main__':
    obj = SmallestInfiniteSet()
    print(obj.popSmallest())
    print(obj.popSmallest())
    print(obj.popSmallest())
    obj.addBack(2)
    print(obj.popSmallest())
