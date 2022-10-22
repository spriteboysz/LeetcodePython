#!/usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-01-22 23:50:16
LastEditTime: 2022-01-22 23:51:43
Description:
FilePath: 1920.基于排列构建数组.py
"""

from typing import List


class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        return [nums[i] for i in nums]


if __name__ == '__main__':
    solution = Solution().buildArray([5, 0, 1, 2, 3, 4])
    print(solution)
