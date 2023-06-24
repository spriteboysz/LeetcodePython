#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2023-06-24 21:58
FileName: algorithm/P2733. 既不是最小值也不是最大值.py
Description: 
"""
from typing import List


class Solution:
    def findNonMinOrMax(self, nums: List[int]) -> int:
        minimum, maximum = min(nums), max(nums)
        for num in nums:
            if num != minimum and num != maximum:
                return num
        return -1


if __name__ == '__main__':
    print(Solution().findNonMinOrMax(nums=[3, 2, 1, 4]))
