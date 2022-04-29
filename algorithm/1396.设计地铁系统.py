#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-03-06 22:06:53
LastEditTime: 2022-04-29 22:50:02
Description: 
FilePath: 1396.设计地铁系统.py
"""
#
# @lc app=leetcode.cn id=1396 lang=python3
#
# [1396] 设计地铁系统
#

# @lc code=start
from collections import defaultdict


class UndergroundSystem:
    def __init__(self):
        self.id = defaultdict(list)
        self.time = defaultdict(list)

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.id[id].extend([stationName, t])

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        self.time[(self.id[id][0], stationName)].append(t - self.id[id][1])
        self.id.pop(id)

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        time = self.time[(startStation, endStation)]
        return sum(time) / len(time)


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)
# @lc code=end
