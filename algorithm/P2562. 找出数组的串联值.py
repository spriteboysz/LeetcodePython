#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2023-05-04 23:31
FileName: algorithm/P2562. 找出数组的串联值.py
Description: 
"""
from typing import List


class Solution:
    def findTheArrayConcVal(self, nums: List[int]) -> int:
        n, val = len(nums), 0
        for i in range(0, n // 2):
            val += int(str(nums[i]) + str(nums[-1 - i]))
        return val if n % 2 == 0 else val + nums[n // 2]


if __name__ == '__main__':
    print(Solution().findTheArrayConcVal(nums=[7, 52, 2, 4]))
    print(Solution().findTheArrayConcVal(nums=[5, 14, 13, 8, 12]))
