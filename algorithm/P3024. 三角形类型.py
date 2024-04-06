#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-04-06 14:10
FileName: algorithm
Description:P3024. 三角形类型.py 
"""
from typing import List


class Solution:
    def triangleType(self, nums: List[int]) -> str:
        nums.sort()
        if nums[0] + nums[1] <= nums[2]:
            return 'none'
        return ['scalene', 'equilateral', 'isosceles'][len(set(nums)) % 3]


if __name__ == '__main__':
    print(Solution().triangleType(nums=[3, 3, 3]))
