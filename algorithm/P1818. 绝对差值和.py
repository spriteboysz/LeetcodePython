#!/usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-02-12 17:14:04
LastEditTime: 2022-02-12 17:34:51
Description:
FilePath: 1818.绝对差值和.py
"""
#
# @lc app=leetcode.cn id=1818 lang=python3
#
# [1818] 绝对差值和
#

# @lc code=start
from typing import List


class Solution:
    def minAbsoluteSumDiff(self, nums1: List[int], nums2: List[int]) -> int:
        absolute = list(map(lambda el1, el2: abs(el1 - el2), nums1, nums2))
        maximum = max(absolute)
        maxindex = absolute.index(maximum)
        minmum = min(map(lambda el: abs(el - nums2[maxindex]), nums1))
        print(sum(absolute), maximum, minmum)
        return (sum(absolute) - maximum + minmum) % (10 ** 9 + 7)
# @lc code=end


if __name__ == "__main__":
    s = Solution()
    # print(s.minAbsoluteSumDiff([1, 7, 5], [2, 3, 5]))
    # print(s.minAbsoluteSumDiff(nums1=[2, 4, 6, 8, 10], nums2=[2, 4, 6, 8, 10]))
    # print(s.minAbsoluteSumDiff(
    #     nums1=[1, 10, 4, 4, 2, 7], nums2=[9, 3, 5, 1, 7, 4]))
    print(s.minAbsoluteSumDiff([1, 28, 21], [9, 21, 20]))
