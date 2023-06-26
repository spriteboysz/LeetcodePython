#!/usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-01-22 21:42:24
LastEditTime: 2022-01-22 21:51:38
Description:
FilePath: 2032.至少在两个数组中出现的值.py
"""
#
# @lc app=leetcode.cn id=2032 lang=python3
#
# [2032] 至少在两个数组中出现的值
#

# @lc code=start
from typing import List


class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        nums = list(set(nums1 + nums2 + nums3))
        common = []
        for num in nums:
            if int(num in nums1) + int(num in nums2) + int(num in nums3) >= 2:
                common.append(num)
        return common

# @lc code=end


if __name__ == "__main__":
    s = Solution()
    print(s.twoOutOfThree(nums1=[1, 2, 2], nums2=[4, 3, 3], nums3=[5]))
    print(s.twoOutOfThree(nums1=[3, 1], nums2=[2, 3], nums3=[1, 2]))
