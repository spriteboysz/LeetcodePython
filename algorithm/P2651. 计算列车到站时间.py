#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2023-05-03 22:19
FileName: algorithm/P2651. 计算列车到站时间.py
Description: 
"""


class Solution:
    def findDelayedArrivalTime(self, arrivalTime: int, delayedTime: int) -> int:
        return (arrivalTime + delayedTime) % 24


if __name__ == '__main__':
    print(Solution().findDelayedArrivalTime(arrivalTime=13, delayedTime=11))
