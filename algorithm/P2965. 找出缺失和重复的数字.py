#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-01-01 22:00
FileName: algorithm
Description:P2965. 找出缺失和重复的数字.py 
"""
from typing import List


class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        nums = [0] * len(grid[0]) ** 2
        for row in grid:
            for num in row:
                nums[num - 1] += 1
        a, b = -1, -1
        for i, v in enumerate(nums):
            if v == 2:
                a = i + 1
            if v == 0:
                b = i + 1
        return [a, b]


if __name__ == '__main__':
    print(Solution().findMissingAndRepeatedValues(grid=[[9, 1, 7], [8, 9, 2], [3, 4, 6]]))
