#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2023/1/28 23:31
FileName: algorithm/P2475. 数组中不等三元组的数目.py
Description: 
"""
from typing import List


class Solution:
    def unequalTriplets(self, nums: List[int]) -> int:
        cnt, n = 0, len(nums)
        for i in range(n):
            for j in range(i + 1, n):
                if nums[i] == nums[j]: continue
                for k in range(j + 1, n):
                    if nums[i] != nums[k] and nums[j] != nums[k]:
                        cnt += 1
        return cnt


if __name__ == '__main__':
    print(Solution().unequalTriplets(nums=[4, 4, 2, 4, 3]))
