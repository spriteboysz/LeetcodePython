#!/usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-01-24 23:38:11
LastEditTime: 2022-01-24 23:43:43
Description:
FilePath: 1603.设计停车系统.py
"""
#
# @lc app=leetcode.cn id=1603 lang=python3
#
# [1603] 设计停车系统
#

# @lc code=start


class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self.park = [None, big, medium, small]

    def addCar(self, carType: int) -> bool:
        if self.park[carType] > 0:
            self.park[carType] -= 1
            return True
        else:
            return False


# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)
# @lc code=end
