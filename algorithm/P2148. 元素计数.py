#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2023-07-11 23:04
FileName: algorithm/P2148. 元素计数.py
Description: 
"""
from typing import List


class Solution:
    def countElements(self, nums: List[int]) -> int:
        return max(0, len(nums) - nums.count(min(nums)) - nums.count(max(nums)))


if __name__ == '__main__':
    print(Solution().countElements(nums=[11, 7, 2, 15]))
