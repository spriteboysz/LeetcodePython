#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-04-06 17:22
FileName: algorithm
Description:P3038. 相同分数的最大操作数目 I.py 
"""
from typing import List


class Solution:
    def maxOperations(self, nums: List[int]) -> int:
        target = sum(nums[:2])
        for i in range(2, len(nums) - 1, 2):
            if nums[i] + nums[i + 1] != target:
                return i // 2
        return len(nums) // 2


if __name__ == '__main__':
    print(Solution().maxOperations(nums=[3, 2, 1, 4, 2, 3, 1, 5, 5]))
