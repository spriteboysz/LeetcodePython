#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2023-07-11 22:56
FileName: algorithm/P1685. 有序数组中差绝对值之和.py
Description:1685. 有序数组中差绝对值之和
"""
from typing import List


class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [0] * n
        for i in range(n):
            res[0] += (nums[i] - nums[0])
        for i in range(1, n):
            res[i] = res[i - 1] + (nums[i] - nums[i - 1]) * (2 * i - n)
        return res


if __name__ == '__main__':
    print(Solution().getSumAbsoluteDifferences(nums=[1, 4, 6, 8, 10]))
