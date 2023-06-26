#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2023-06-25 21:52
FileName: algorithm/P2740. 找出分区值.py
Description: 
"""
from typing import List


class Solution:
    def findValueOfPartition(self, nums: List[int]) -> int:
        nums.sort()
        minimum = nums[1] - nums[0]
        for i in range(2, len(nums)):
            minimum = min(minimum, nums[i] - nums[i - 1])
        return minimum


if __name__ == '__main__':
    print(Solution().findValueOfPartition(nums=[1, 3, 2, 4]))
