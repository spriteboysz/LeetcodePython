#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-04-24 22:26:41
LastEditTime: 2022-04-24 22:34:40
Description: 
FilePath: 1577.数的平方等于两数乘积的方法数.py
"""
#
# @lc app=leetcode.cn id=1577 lang=python3
#
# [1577] 数的平方等于两数乘积的方法数
#

from collections import Counter
# @lc code=start
from typing import List


class Solution:
    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        dic1 = Counter([num ** 2 for num in nums1])
        dic2 = Counter([num ** 2 for num in nums2])
        count = 0
        for i in range(len(nums2)):
            for j in range(i + 1, len(nums2)):
                if nums2[i] * nums2[j] in dic1:
                    count += dic1[nums2[i] * nums2[j]]
        for i in range(len(nums1)):
            for j in range(i + 1, len(nums1)):
                if nums1[i] * nums1[j] in dic2:
                    count += dic2[nums1[i] * nums1[j]]
        return count


# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    ans = solution.numTriplets(nums1=[7, 4], nums2=[5, 2, 8, 9])
    print(ans)
