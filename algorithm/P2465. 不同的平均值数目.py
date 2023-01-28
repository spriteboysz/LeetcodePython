#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2023/1/28 23:52
FileName: algorithm/P2465. 不同的平均值数目.py
Description: 
"""
from typing import List


class Solution:
    def distinctAverages(self, nums: List[int]) -> int:
        nums.sort()
        average = set()
        for i in range(len(nums) // 2):
            average.add(nums[i] + nums[len(nums) - i - 1])
        return len(average)


if __name__ == '__main__':
    print(Solution().distinctAverages([4, 1, 4, 0, 3, 5]))
