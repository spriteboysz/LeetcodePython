#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2023-05-04 23:10
FileName: algorithm/P2574. 左右元素和的差值.py
Description: 
"""
from typing import List


class Solution:
    def leftRigthDifference(self, nums: List[int]) -> List[int]:
        total, acc = sum(nums), 0
        for i, num in enumerate(nums):
            total -= num
            nums[i] = abs(acc - total)
            acc += num
        return nums


if __name__ == '__main__':
    print(Solution().leftRigthDifference(nums=[10, 4, 8, 3]))
