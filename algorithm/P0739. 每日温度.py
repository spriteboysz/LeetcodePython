#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-05-03 11:53
FileName: algorithm
Description:P0739. 每日温度.py 
"""
from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        daily, stack = [0] * len(temperatures), []
        for i, temperature in enumerate(temperatures):
            while stack and temperature > temperatures[stack[-1]]:
                prev_index = stack.pop()
                daily[prev_index] = i - prev_index
            stack.append(i)
        return daily


if __name__ == '__main__':
    print(Solution().dailyTemperatures(temperatures=[73, 74, 75, 71, 69, 72, 76, 73]))
