#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2023/2/1 22:53
FileName: algorithm/P2335. 装满杯子需要的最短总时长.py
Description: 
"""
from typing import List
from math import ceil


class Solution:
    def fillCups(self, amount: List[int]) -> int:
        return max(max(amount), ceil(sum(amount) / 2))


if __name__ == '__main__':
    print(Solution().fillCups(amount=[1, 4, 2]))
