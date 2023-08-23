#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2023-08-23 23:19
FileName: algorithm
Description:P2784. 检查数组是否是好的.py 
"""
from typing import List


class Solution:
    def isGood(self, nums: List[int]) -> bool:
        nums.sort()
        for i in range(len(nums) - 1):
            if nums[i] != i + 1:
                return False
        return nums[-1] == len(nums) - 1


if __name__ == '__main__':
    print(Solution().isGood(nums=[1, 3, 3, 2]))
