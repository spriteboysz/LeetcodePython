#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-05-29 22:17
LastEditTime: 2022-05-29 22:17
Description:
FilePath: 剑指 Offer II 059. 数据流的第 K 大数值.py
"""

from heapq import heappush, heappop
from typing import List

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.queue = []
        for num in nums:
            heappush(self.queue, num)
            if len(self.queue) > k:
                heappop(self.queue)

    def add(self, val: int) -> int:
        heappush(self.queue, val)
        if len(self.queue) > self.k:
            heappop(self.queue)
        return self.queue[0]

# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
