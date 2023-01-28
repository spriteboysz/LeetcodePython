#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2023/1/28 23:56
FileName: algorithm/P2460. 对数组执行操作.py
Description: 
"""
from typing import List


class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        i = 0
        while i < len(nums) - 1:
            if nums[i] == nums[i + 1] and nums[i] > 0:
                nums[i], nums[i + 1] = nums[i] * 2, 0
                i += 1
            i += 1
        return sorted(nums, key=lambda item: 0 if item > 0 else 1)


if __name__ == '__main__':
    print(Solution().applyOperations([1, 2, 2, 1, 1, 0]))
