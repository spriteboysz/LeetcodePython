#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-04-09 23:52:00
LastEditTime: 2022-04-09 23:55:05
Description: 
FilePath: 478.在圆内随机生成点.py
"""
#
# @lc app=leetcode.cn id=478 lang=python3
#
# [478] 在圆内随机生成点
#

from math import sin, cos, sqrt, pi
# @lc code=start
from random import uniform
from typing import List


class Solution:
    def __init__(self, radius: float, x_center: float, y_center: float):
        self.radius = radius
        self.x, self.y = x_center, y_center

    def randPoint(self) -> List[float]:
        r, theta = sqrt(uniform(0, 1)) * self.radius, uniform(0, 2 * pi)
        return [self.x + r * sin(theta), self.y + r * cos(theta)]

# Your Solution object will be instantiated and called as such:
# obj = Solution(radius, x_center, y_center)
# param_1 = obj.randPoint()
# @lc code=end
