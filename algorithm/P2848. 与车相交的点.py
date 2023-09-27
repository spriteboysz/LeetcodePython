#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2023-09-24 22:16
FileName: algorithm
Description:P2848. 与车相交的点.py 
"""
from typing import List


class Solution:
    def numberOfPoints(self, nums: List[List[int]]) -> int:
        seen = set()
        for left, right in nums:
            for num in range(left, right + 1):
                seen.add(num)
        return len(seen)


if __name__ == '__main__':
    print(Solution().numberOfPoints(nums=[[1, 3], [5, 8]]))
