#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-01-01 21:38
FileName: algorithm
Description:P2974. 最小数字游戏.py 
"""
from typing import List


class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        nums.sort()
        for i in range(0, len(nums), 2):
            nums[i], nums[i + 1] = nums[i + 1], nums[i]
        return nums


if __name__ == '__main__':
    print(Solution().numberGame(nums=[5, 4, 2, 3]))
