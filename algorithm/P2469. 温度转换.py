#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022/12/3 21:55
FileName: algorithm/P2469. 温度转换.py
Description: 
"""
from typing import List


class Solution:
    def convertTemperature(self, celsius: float) -> List[float]:
        return [celsius + 273.15, celsius * 1.8 + 32.00]


if __name__ == '__main__':
    print(Solution().convertTemperature(36.5))
