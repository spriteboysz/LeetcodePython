#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-05-18 16:17
FileName: algorithm
Description:P1798. 你能构造出连续值的最大数目.py 
"""
from typing import List


class Solution:
    def getMaximumConsecutive(self, coins: List[int]) -> int:
        m = 0
        coins.sort()
        for coin in coins:
            if coin - m > 1:
                break
            m += coin
        return m + 1


if __name__ == '__main__':
    print(Solution().getMaximumConsecutive(coins=[1, 1, 1, 4]))
