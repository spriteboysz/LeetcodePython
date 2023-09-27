#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2023-09-24 22:00
FileName: algorithm
Description:P2855. 使数组成为递增数组的最少右移次数.py 
"""
from typing import List


class Solution:
    def minimumRightShifts(self, nums: List[int]) -> int:
        nums2 = sorted(nums)
        s1 = "#".join(map(str, nums))
        s2 = "#".join(map(str, nums2))
        if s1 in s2 + "#" + s2:
            return nums2.index(nums[0])
        else:
            return -1


if __name__ == '__main__':
    print(Solution().minimumRightShifts(nums=[3, 4, 5, 1, 2]))
