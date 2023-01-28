#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2023/1/28 23:18
FileName: algorithm/P2529. 正整数和负整数的最大计数.py
Description: 
"""
from typing import List


class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        positive, negative = 0, 0
        for num in nums:
            if num > 0:
                positive += 1
            elif num < 0:
                negative += 1
        return max(positive, negative)


if __name__ == '__main__':
    print(Solution().maximumCount([-2, -1, -1, 1, 2, 3]))
