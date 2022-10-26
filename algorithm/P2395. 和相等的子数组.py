#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-10-26 22:18
FileName: algorithm/P2395. 和相等的子数组.py
Description: 
"""
from typing import List


class Solution:
    def findSubarrays(self, nums: List[int]) -> bool:
        sum = set()
        for i in range(1, len(nums)):
            if (nums[i - 1] + nums[i]) in sum:
                return True
            else:
                sum.add(nums[i - 1] + nums[i])
        return False


if __name__ == '__main__':
    print(Solution().findSubarrays(nums=[4, 2, 4]))
