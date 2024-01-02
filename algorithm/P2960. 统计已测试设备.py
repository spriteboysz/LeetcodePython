#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-01-01 22:30
FileName: algorithm
Description:P2960. 统计已测试设备.py 
"""
from typing import List


class Solution:
    def countTestedDevices(self, batteryPercentages: List[int]) -> int:
        cnt = 0
        for i in range(len(batteryPercentages)):
            if batteryPercentages[i] > 0:
                cnt += 1
                for j in range(i + 1, len(batteryPercentages)):
                    batteryPercentages[j] -= 1
        return cnt


if __name__ == '__main__':
    print(Solution().countTestedDevices(batteryPercentages=[1, 1, 2, 1, 3]))
