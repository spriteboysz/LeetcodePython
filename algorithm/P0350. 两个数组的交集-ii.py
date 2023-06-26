#!/usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-01-15 22:00:16
LastEditTime: 2022-01-15 22:26:40
Description:
FilePath: 350.两个数组的交集-ii.py
"""
#
# @lc app=leetcode.cn id=350 lang=python3
#
# [350] 两个数组的交集 II
#

# @lc code=start
from typing import List


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        intersection = list(set(nums1) & set(nums2))
        count = list(
            map(lambda el: min(nums1.count(el), nums2.count(el)), intersection))
        lst = []
        for i, v in enumerate(intersection):
            lst.extend([str(v)] * count[i])
        return list(map(int, lst))

# @lc code=end


if __name__ == '__main__':
    s = Solution()
    print(s.intersect([4, 9, 5], [9, 4, 9, 8, 4]))
