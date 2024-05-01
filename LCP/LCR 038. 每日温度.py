#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-05-01 21:18
FileName: LCP
Description:LCR 038. 每日温度.py 
"""
from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        days, stack = [0] * len(temperatures), []
        for i, temperature in enumerate(temperatures):
            while stack and temperature > temperatures[stack[-1]]:
                prev = stack.pop()
                days[prev] = i - prev
            stack.append(i)
        return days


if __name__ == '__main__':
    print(Solution().dailyTemperatures(temperatures=[73, 74, 75, 71, 69, 72, 76, 73]))
