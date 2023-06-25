#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2023-06-24 23:10
FileName: algorithm/P2670. 找出不同元素数目差数组.py
Description: 
"""
from typing import List


class Solution:
    def distinctDifferenceArray(self, nums: List[int]) -> List[int]:
        return [len(set(nums[:i + 1])) - len(set(nums[i + 1:])) for i in range(0, len(nums))]


if __name__ == '__main__':
    print(Solution().distinctDifferenceArray(nums=[1, 2, 3, 4, 5]))
