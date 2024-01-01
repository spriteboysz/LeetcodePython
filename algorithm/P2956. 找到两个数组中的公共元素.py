#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-01-01 22:39
FileName: algorithm
Description:P2956. 找到两个数组中的公共元素.py 
"""
from typing import List


class Solution:
    def findIntersectionValues(self, nums1: List[int], nums2: List[int]) -> List[int]:
        set1, set2 = set(nums1), set(nums2)
        a, b = 0, 0
        for num in nums1:
            if num in set2:
                a += 1
        for num in nums2:
            if num in set1:
                b += 1
        return [a, b]


if __name__ == '__main__':
    print(Solution().findIntersectionValues(nums1=[4, 3, 2, 3, 1], nums2=[2, 2, 5, 2, 3, 6]))
