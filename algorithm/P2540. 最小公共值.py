#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2023/1/29 0:00
FileName: algorithm/P2540. 最小公共值.py
Description: 
"""
from typing import List


class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        set1 = set(nums1)
        for num in nums2:
            if num in set1:
                return num
        else:
            return -1


if __name__ == '__main__':
    print(Solution().getCommon(nums1=[1, 2, 3, 6], nums2=[2, 3, 4, 5]))
