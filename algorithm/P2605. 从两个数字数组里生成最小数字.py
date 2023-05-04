#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2023-05-03 23:28
FileName: algorithm/P2605. 从两个数字数组里生成最小数字.py
Description: 
"""
from typing import List


class Solution:
    def minNumber(self, nums1: List[int], nums2: List[int]) -> int:
        digits = [0] * 10
        for num in nums1:
            digits[num] |= 1
        for num in nums2:
            digits[num] |= 2
        a, b = 0, 0
        for i, digit in enumerate(digits):
            if digit == 3:
                return i
            if a == 0 and digit == 1:
                a = i
            if b == 0 and digit == 2:
                b = i
        return min(a * 10 + b, a + b * 10)


if __name__ == '__main__':
    print(Solution().minNumber(nums1=[4, 1, 3], nums2=[5, 7]))
