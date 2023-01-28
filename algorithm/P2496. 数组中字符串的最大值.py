#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2023/1/28 23:20
FileName: algorithm/P2496. 数组中字符串的最大值.py
Description: 
"""
from typing import List


class Solution:
    def maximumValue(self, strs: List[str]) -> int:
        maximum = -1
        for item in strs:
            try:
                maximum = max(maximum, int(item))
            except ValueError:
                maximum = max(maximum, len(item))
        return maximum


if __name__ == '__main__':
    print(Solution().maximumValue(["alic3", "bob", "3", "4", "00000"]))
