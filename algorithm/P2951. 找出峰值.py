#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-01-01 22:43
FileName: algorithm
Description:P2951. 找出峰值.py 
"""
from typing import List


class Solution:
    def findPeaks(self, mountain: List[int]) -> List[int]:
        peaks = []
        for i in range(1, len(mountain) - 1):
            if mountain[i] > mountain[i - 1] and mountain[i] > mountain[i + 1]:
                peaks.append(i)
        return peaks


if __name__ == '__main__':
    print(Solution().findPeaks(mountain=[1, 4, 3, 8, 5]))
