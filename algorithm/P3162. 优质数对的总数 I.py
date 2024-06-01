#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-06-01 22:22
FileName: algorithm
Description:P3162. 优质数对的总数 I.py 
"""
from typing import List


class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], k: int) -> int:
        return sum([1 for num1 in nums1 for num2 in nums2 if num1 % (num2 * k) == 0])


if __name__ == '__main__':
    print(Solution().numberOfPairs(nums1=[1, 3, 4], nums2=[1, 3, 4], k=1))
