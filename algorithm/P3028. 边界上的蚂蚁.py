#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-04-06 14:21
FileName: algorithm
Description:P3028. 边界上的蚂蚁.py 
"""
from typing import List


class Solution:
    def returnToBoundaryCount(self, nums: List[int]) -> int:
        acc, cnt = 0, 0
        for num in nums:
            acc += num
            if acc == 0:
                cnt += 1
        return cnt


if __name__ == '__main__':
    print(Solution().returnToBoundaryCount(nums=[2, 3, -5]))
