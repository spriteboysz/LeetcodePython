#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-05-22 21:46
FileName: algorithm
Description:P3151. 特殊数组 I.py 
"""
from typing import List


class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        ss = ''.join(map(str, [num % 2 for num in nums]))
        return '00' not in ss and '11' not in ss


if __name__ == '__main__':
    print(Solution().isArraySpecial(nums=[2, 1, 4]))
