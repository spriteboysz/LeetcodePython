#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2023-05-04 23:39
FileName: algorithm/P2558. 从数量最多的堆取走礼物.py
Description: 
"""
import math
from typing import List


class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        for i in range(0, k):
            gifts.sort()
            gifts[-1] = int(math.sqrt(gifts[-1]))
        return sum(gifts)


if __name__ == '__main__':
    print(Solution().pickGifts(gifts=[25, 64, 9, 4, 100], k=4))
