#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-05-01 19:48
FileName: algorithm
Description:P3131. 找出与数组相加的整数 I.py 
"""
from typing import List


class Solution:
    def addedInteger(self, nums1: List[int], nums2: List[int]) -> int:
        return max(nums2) - max(nums1)


if __name__ == '__main__':
    print(Solution().addedInteger(nums1=[2, 6, 4], nums2=[9, 7, 5]))
