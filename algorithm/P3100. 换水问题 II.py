#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-05-12 11:03
FileName: algorithm
Description:P3100. 换水问题 II.py 
"""


class Solution:
    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:
        bottles = numBottles
        while numBottles >= numExchange:
            bottles += 1
            numBottles += 1 - numExchange
            numExchange += 1
        return bottles


if __name__ == '__main__':
    print(Solution().maxBottlesDrunk(numBottles=10, numExchange=3))
