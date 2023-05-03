#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2023-05-03 22:11
FileName: algorithm/P2656. K 个元素的最大和.py
Description: 
"""
from typing import List


class Solution:
    def maximizeSum(self, nums: List[int], k: int) -> int:
        return max(nums) * k + (k - 1) * k // 2


if __name__ == '__main__':
    print(Solution().maximizeSum(nums=[1, 2, 3, 4, 5], k=3))
