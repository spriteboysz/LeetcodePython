#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2022-02-09 21:43:53
LastEditTime: 2022-02-09 22:15:02
Description: 
FilePath: 1845.座位预约管理系统.py
'''
#
# @lc app=leetcode.cn id=1845 lang=python3
#
# [1845] 座位预约管理系统
#

# @lc code=start
import heapq


class SeatManager:

    def __init__(self, n: int):
        self.seats = [i for i in range(1, n + 1)]

    def reserve(self) -> int:
        return heapq.heappop(self.seats)

    def unreserve(self, seatNumber: int) -> None:
        heapq.heappush(self.seats, seatNumber)


# Your SeatManager object will be instantiated and called as such:
# obj = SeatManager(n)
# param_1 = obj.reserve()
# obj.unreserve(seatNumber)
# @lc code=end
